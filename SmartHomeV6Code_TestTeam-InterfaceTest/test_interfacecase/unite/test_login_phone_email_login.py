#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_phone_email_login import Login_phone_email_login
import unittest

class Login_phone_email_loginTestCase(unittest.TestCase):
    def setUp(self):
        self.loginphoneemaillogin = Login_phone_email_login()

    def test_login_phone_email_login(self):
        u""""验证码登录"""
        self.assertEqual(self.loginphoneemaillogin.login_phone_email_login(),"0")

    def tearDown(self):
        self.loginphoneemaillogin = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login_phone_email_loginTestCase("test_login_phone_email_login"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
