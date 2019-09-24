#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_phone_email_sendCode import Login_phone_email_sendCode
import unittest

class Login_phone_email_sendCodeTestCase(unittest.TestCase):
    def setUp(self):
        self.loginphoneemailsendCode = Login_phone_email_sendCode()

    def test_login_phone_email_sendCode(self):
        u""""验证码登录发送验证码"""
        self.assertEqual(self.loginphoneemailsendCode.login_phone_email_sendCode(),"0")

    def tearDown(self):
        self.loginphoneemailsendCode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login_phone_email_sendCodeTestCase("test_login_phone_email_sendCode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
