#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_oss_ram_account import Users_uId_oss_ram_account
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_oss_ram_accountTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdossramaccount = Users_uId_oss_ram_account()
        self.loginlogout = Login_logout()


    def test_users_uId_oss_ram_account(self):
        u""""获取爱看OSS子账号数据"""
        self.assertEqual(self.usersuIdossramaccount.users_uId_oss_ram_account(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdossramaccount= None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_oss_ram_accountTestCase("test_users_uId_oss_ram_account"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)