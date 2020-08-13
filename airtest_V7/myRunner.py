# coding=utf-8

"""
作者: Duke
文件名: myRunner.py
创建时间: 2020/08/06-10:43
"""

from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
from conf.settings import *
import jinja2, shutil, os, io, datetime


class Runing(AirtestCase):
    def setUp(self):
        print('-------小火车开起来-------')
        super(Runing, self).setUp()

    def tearDown(self):
        print('------滴滴滴，到站了-------')
        super(Runing, self).setUp()

    @staticmethod
    def run_air(air_dir, device):

        start_time = datetime.datetime.now()
        start_time_fmt = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        # 聚合结果
        results = []
        # 获取所有用例集
        if os.path.isdir(log_path):
            shutil.rmtree(log_path)
        else:
            os.makedirs(log_path)

        for file in os.listdir(air_dir):
            if file.endswith('.air'):
                # f为.air测试用例名称:test1.air
                airName = file
                airDirName = file.replace('.air', '')
                # script为.air的全路径:D:\test\airtest_V7\test_case\test1.air
                script = os.path.join(air_dir, file)
                # air_log为日志存放路径和名称
                air_log = log_path + "\\" + airDirName
                # 判断case日志在不在，在，则删除目录中的内容，否则，新建每个脚本log目录
                if os.path.isdir(air_log):
                    print(air_log)
                    shutil.rmtree(air_log)
                else:
                    os.makedirs(air_log)

                # 日志输出文件log：D:\test\airtest_V7\test_case\log\test1\log.html
                output_file1 = air_log + '\\' + 'log.html'
                # 命令行参数，解析获得后的数据格式Namespace(device=device, log=log, recording=None, script=script)
                # args = Namespace(device=device, log=log, recording=None, script=script)
                args = Namespace(device=device, log=air_log, recording=None, script=script, compress=10)
                try:
                    run_script(args, AirtestCase)
                except AssertionError:
                    pass
                finally:
                    rpt = report.LogToHtml(script, air_log)
                    # 结果模板渲染，“log_template.html”自带的模板，output_file日志存放路径
                    rpt.report("log_template.html", output_file=output_file1)
                    # 结果保存在result对象中
                    # result = {}
                    result = dict()
                    result['name'] = airName.replace('.air', '')
                    result['result'] = rpt.test_result
                    results.append(result)

        end_time = datetime.datetime.now()
        end_time_fmt = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        duration = (end_time - start_time).seconds
        # 根据summary_template.html模板，生成聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            extensions=(),
            autoescape=True
        )

        template = env.get_template(template_name, template_path)
        success = 0
        fail = 0
        for res in results:
            if res['result']:
                success += 1
            else:
                fail += 1
        report_name = 'report' + end_time.strftime("%Y%m%d%H%M%S") + ".html"
        html = template.render(
            {"results": results, 'device': phone, "stime": start_time_fmt, 'etime': end_time_fmt,
             'duration': duration,
             "project": project_name, "success": success, "fail": fail})
        output_file2 = os.path.join(report_path, report_name)
        with io.open(output_file2, 'w', encoding='utf-8') as f:
            f.write(html)


if __name__ == '__main__':
    test = Runing()
    test.run_air(air_path, devices)

# python myRunner.py
