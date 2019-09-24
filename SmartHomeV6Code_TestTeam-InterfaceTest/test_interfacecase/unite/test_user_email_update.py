#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.user_email_update import User_email_update
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_email_updateTestCase(unittest.TestCase):
    def setUp(self):
        self.useremailupdate = User_email_update()
        self.loginlogout = Login_logout()


    def test_user_email_update(self):
        u""""变更邮箱发送邮箱验证码到新邮箱和绑定新邮箱"""
        self.assertEqual(self.useremailupdate.user_email_update(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.useremailupdate= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_email_updateTestCase("test_user_email_update"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)