#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_member_point_info import User_member_point_info
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_member_point_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.usermemberpointinfo = User_member_point_info()
        self.loginlogout = Login_logout()

    def test_user_member_point_info(self):
        u""""获取当前用户的积分信息(当前积分、累计积分、会员级别)"""
        self.assertEqual(self.usermemberpointinfo.user_member_point_info(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usermemberpointinfo = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_member_point_infoTestCase("test_user_member_point_info"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)