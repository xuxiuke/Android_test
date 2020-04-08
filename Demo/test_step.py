#coding=utf-8

"""
作者: Duke
文件名: test_step.py
创建时间: 2020/04/08-08:58
"""

from Demo import step
from Demo.open_baidu import Open_baidu
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test001(unittest.TestCase, step.Login):  # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_baidu(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、账号已有住宅情况，登录成功
    def test_login_success(self):
        self.assertTrue(self.login_success())