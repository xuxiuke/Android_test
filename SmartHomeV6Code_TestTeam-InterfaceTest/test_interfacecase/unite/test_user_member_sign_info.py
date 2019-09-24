#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_member_sign_info import User_member_sign_info
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_member_sign_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.usermembersigninfo = User_member_sign_info()
        self.loginlogout = Login_logout()


    def test_user_member_sign_info(self):
        u""""获取当前用户的签到信息"""
        self.assertEqual(self.usermembersigninfo.user_member_sign_info() , "0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.user_member_sign_info= None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_member_sign_infoTestCase("test_user_member_sign_info"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)

