#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_member_point_history import User_member_point_history
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_member_point_historyTestCase(unittest.TestCase):
    def setUp(self):
        self.usermemberpointhistory = User_member_point_history()
        self.loginlogout = Login_logout()

    def test_user_member_point_history(self):
        u""""获取当前用户的积分增加与消费记录"""
        self.assertEqual(self.usermemberpointhistory.user_member_point_history(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usermemberpointhistory = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_member_point_historyTestCase("test_user_member_point_history"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)