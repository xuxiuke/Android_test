#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_byemail import Login_byemail
import unittest
from test_interfacecase.public.login_logout import Login_logout
from test_interfacecase.bussiness import global_value


class Login_byemailTestCase(unittest.TestCase):
    def setUp(self):
        self.loginbymail = Login_byemail()


    def test_login_byemail(self):
        u""""邮箱登录账号"""
        self.assertEqual(self.loginbymail.login_byemail(),"0")

    def tearDown(self):
        self.loginbymail = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login_byemailTestCase("test_login_byemail"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)