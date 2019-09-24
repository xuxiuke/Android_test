#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_logout import Login_logout
import unittest

class Login_logoutTestCase(unittest.TestCase):
    def setUp(self):
        self.loginlogout = Login_logout()

    def test_login_logout(self):
        u""""退出登录"""
        self.assertEqual(self.loginlogout.login_logout(),"0")

    def tearDown(self):
        self.loginlogout = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login_logoutTestCase("test_login_logout"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
