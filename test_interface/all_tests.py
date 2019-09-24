# coding=utf-8

"""
作者: Duke
文件名: all_tests.py
创建时间: 2019/09/12-10:03
"""


import unittest
import HTMLTestRunner
import os
import time
from public.send_email import send_email

# 相对路径
testcase_path = '.\\test'
report_path = '.\\report'

def creat_suite():
    uit = unittest.TestSuite()
    # defaultTestLoader()类，通过该类下面的discover()方法可自动根据测试目录testcase_path匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test_*.py')
    for test_suite in discover:
        # print(test_suite)
        for test_case in test_suite:
            uit.addTest(test_case)  # 添加类中的测试用例
    return uit

suite = creat_suite()

now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))  # 获取系统当前时间
resultname = os.path.join(report_path + '\\' 'wuliancloud_interfacetest' + now + '.html')  # 'result.html'
file_result = open(resultname, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title="物联云接口测试报告", description="用例执行情况:")
runner.run(suite)
file_result.close()
send_email()

