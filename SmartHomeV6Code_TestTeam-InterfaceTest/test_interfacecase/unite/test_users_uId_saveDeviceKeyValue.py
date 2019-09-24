#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_saveDeviceKeyValue import Users_uId_saveDeviceKeyValue
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_saveDeviceKeyValueTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdsaveDeviceKeyValue = Users_uId_saveDeviceKeyValue()
        self.loginlogout = Login_logout()


    def test_users_uId_saveDeviceKeyValue(self):
        u""""保存设备键值对信息"""
        self.assertEqual(self.usersuIdsaveDeviceKeyValue.users_uId_saveDeviceKeyValue(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdsaveDeviceKeyValue= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_saveDeviceKeyValueTestCase("test_users_uId_saveDeviceKeyValue"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)