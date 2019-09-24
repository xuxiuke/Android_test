#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.user_info import User_info
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.userinfo = User_info()
        self.loginlogout = Login_logout()


    def test_user_info(self):
        u""""api接口-获取当前登录用户的用户信息"""
        self.assertEqual(self.userinfo.user_info(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userinfo= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_infoTestCase("test_user_info"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)