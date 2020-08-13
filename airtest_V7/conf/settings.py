#coding=utf-8

"""
作者: Duke
文件名: settings.py
创建时间: 2020/08/10-11:41
"""

import os

project_name = '哆啦AI家V7.0.9自动化测试报告'                                             # 测试报告标题

deviceType = "app"                                                              # 设备类别：app、win和web
devices = ['Android://127.0.0.1:5037/TPE9X18516W00552']                 		# 设备信息，只有当deviceType为app是有效
phone = "华为畅享8e"                                                              # 手机型号
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         # 工程根目录
air_path = os.path.join(root_path,'test_case')                                  # 脚本目录
log_path = os.path.join(root_path,'log')                                        # 日志目录
template_path = os.path.join(root_path,'template')                              # 测试报告模板目录
report_path = os.path.join(root_path,'report')                                  # 测试报告路径
data_path = os.path.join(root_path, 'data')                                     # 测试数据目录
template_name = "summary_template.html"                                         # 测试报告模板名称
clear_report = False                                                            # 是否清空旧测试报告