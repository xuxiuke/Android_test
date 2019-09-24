#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_sip import Users_uId_sip
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_sipTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdsip = Users_uId_sip()
        self.loginlogout = Login_logout()


    def test_users_uId_sip(self):
        u""""查询用户下绑定的设备信息"""
        self.assertEqual(self.usersuIdsip.users_uId_sip(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdsip= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_sipTestCase("test_users_uId_sip"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)