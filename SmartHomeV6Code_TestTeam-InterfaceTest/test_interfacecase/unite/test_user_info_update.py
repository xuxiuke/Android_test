#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_info_update import User_info_update
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_info_updateTestCase(unittest.TestCase):
    def setUp(self):
        self.userinfoupdate = User_info_update()
        self.loginlogout = Login_logout()

    def test_user_info_update(self):
        u""""修改当前登录用户的用户信息"""
        self.assertEqual(self.userinfoupdate.user_info_update(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userinfoupdate = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_info_updateTestCase("test_user_info_update"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)