#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_third_bind import User_third_bind
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_third_bindTestCase(unittest.TestCase):
    def setUp(self):
        self.userthirdbind = User_third_bind()
        self.loginlogout = Login_logout()

    def test_user_third_bind(self):
        u""""三方账号--绑定三方账号"""
        self.assertEqual(self.userthirdbind.user_third_bind(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userthirdbind = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_third_bindTestCase("test_user_third_bind"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
