#coding=utf-8

"""
作者: Duke
文件名: search.py
创建时间: 2020/04/08-10:10
"""

import unittest
import HTMLTestRunner
import time

# 相对路径
testcase_path = '.\\Demo'
report_path = ".\\  Demo\\appium_report.html"

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
# 获取系统当前时间
now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")
# 下两行，run()方法是运行测试套件的测试用例，入参为suite测试套件。
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="百度search", description="测试结果")
runner.run(suite)
fp.close()