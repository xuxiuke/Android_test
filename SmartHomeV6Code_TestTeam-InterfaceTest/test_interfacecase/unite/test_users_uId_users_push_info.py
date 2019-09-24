#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.users_uId_users_push_info import Users_uId_users_push_info
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_users_push_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIduserspushinfo = Users_uId_users_push_info()
        self.loginlogout = Login_logout()

    def test_users_uId_users_push_info(self):
        u""""保存和更新共用此接口"""
        self.assertEqual(self.usersuIduserspushinfo.users_uId_users_push_info(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIduserspushinfo = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_users_push_infoTestCase("test_users_uId_users_push_info"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)