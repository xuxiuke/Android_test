#coding=utf-8

"""
作者: Duke
文件名: test_app_getAppInfo.py
创建时间: 2019/09/11-17:03
"""

import unittest
from case.app_getAppinfo import App_getAppInfo
from public import global_value
from case.login_logout import Login_logout


class App_getAppInfoTestCase(unittest.TestCase):

    def setUp(self):
        self.appgetAppinfo = App_getAppInfo()
        self.loginlogout = Login_logout()

    def test_app_getAppinfo(self):
        """"api接口-APP检查更新的接口"""
        self.assertEqual(self.appgetAppinfo.app_getAppInfo(), "0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.appgetAppinfo = None
