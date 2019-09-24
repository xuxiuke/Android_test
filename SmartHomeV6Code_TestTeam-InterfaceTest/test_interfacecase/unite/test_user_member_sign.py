#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_member_sign import User_member_sign
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_member_signTestCase(unittest.TestCase):
    def setUp(self):
        self.usermembersign = User_member_sign()
        self.loginlogout = Login_logout()


    def test_user_member_sign(self):
        u""""用户签到"""
        if self.usermembersign.user_member_sign() == "0":
            self.assertEqual("0" , "0")
        else:
            self.assertEqual(self.usermembersign.user_member_sign(), "2000013")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.user_member_sign= None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_member_signTestCase("test_user_member_sign"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)