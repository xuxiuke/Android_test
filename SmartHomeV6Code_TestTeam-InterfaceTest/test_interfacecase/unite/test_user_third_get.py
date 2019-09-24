#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from  test_interfacecase.public.user_third_get import User_third_get
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_third_getTestCase(unittest.TestCase):
    def setUp(self):
        self.userthirdget = User_third_get()
        self.loginlogout = Login_logout()


    def test_user_third_get(self):
        u""""api接口-三方账号--查询已绑定的三方账号"""
        self.assertEqual(self.userthirdget.user_third_get(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userthirdget= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_third_getTestCase("test_user_third_get"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)

