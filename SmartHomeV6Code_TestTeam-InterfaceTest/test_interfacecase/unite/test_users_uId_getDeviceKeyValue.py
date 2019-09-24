#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_getDeviceKeyValue import Users_uId_getDeviceKeyValue
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_getDeviceKeyValueTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdgetDeviceKeyValue = Users_uId_getDeviceKeyValue()
        self.loginlogout = Login_logout()


    def test_users_uId_getDeviceKeyValue(self):
        u""""查询设备键值对信息"""
        self.assertEqual(self.usersuIdgetDeviceKeyValue.users_uId_getDeviceKeyValue(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdgetDeviceKeyValue= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_getDeviceKeyValueTestCase("test_users_uId_getDeviceKeyValue"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)