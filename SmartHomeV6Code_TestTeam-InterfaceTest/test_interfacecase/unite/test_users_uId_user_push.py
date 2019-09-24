#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_user_push import Users_uId_user_push
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_user_pushTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIduserpush = Users_uId_user_push()
        self.loginlogout = Login_logout()


    def test_users_uId_user_push(self):
        u""""通知WiFi设备绑定的用户，有人正绑定他的设备"""
        self.assertEqual(self.usersuIduserpush.users_uId_user_push(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIduserpush= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_user_pushTestCase("test_users_uId_user_push"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)