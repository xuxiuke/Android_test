#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

# Created by 顾洋溢

from  test_interfacecase.public.users_uId_rememberCurrentDevice_verfyPassword import Users_uId_rememberCurrentDevice_verfyPassword
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout



class Users_uId_rememberCurrentDevice_verfyPasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdrememberCurrentDeviceverfyPassword = Users_uId_rememberCurrentDevice_verfyPassword()
        self.loginlogout = Login_logout()

    def test_users_uId_rememberCurrentDevice_verfyPassword(self):
        u""""记录用户当前选中的网关并校验密码"""
        self.assertEqual(self.usersuIdrememberCurrentDeviceverfyPassword.users_uId_rememberCurrentDevice_verfyPassword(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdrememberCurrentDeviceverfyPassword = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_rememberCurrentDevice_verfyPasswordTestCase("test_users_uId_rememberCurrentDevice_verfyPassword"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)