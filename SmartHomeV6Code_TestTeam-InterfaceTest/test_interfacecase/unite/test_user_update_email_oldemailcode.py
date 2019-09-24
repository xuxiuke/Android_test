#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.user_update_email_oldemailcode import User_update_email_oldemailcode
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_update_email_oldemailcodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdateemailoldemailcode = User_update_email_oldemailcode()
        self.loginlogout = Login_logout()


    def test_user_update_email_oldemailcode(self):
        u""""发送修改绑定邮箱的邮件到旧邮箱"""
        self.assertEqual(self.userupdateemailoldemailcode.user_update_email_oldemailcode(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdateemailoldemailcode= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_update_email_oldemailcodeTestCase("test_user_update_email_oldemailcode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)