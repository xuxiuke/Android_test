#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_updatepass_email import User_updatepass_email
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_updatepass_emailTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatepassemail = User_updatepass_email()
        self.loginlogout = Login_logout()

    def test_user_updatepass_email(self):
        u""""申请修改用户密码邮件(通过邮箱修改密码)"""
        self.assertEqual(self.userupdatepassemail.user_updatepass_email(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdatepassemail = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_updatepass_emailTestCase("test_user_updatepass_email"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)