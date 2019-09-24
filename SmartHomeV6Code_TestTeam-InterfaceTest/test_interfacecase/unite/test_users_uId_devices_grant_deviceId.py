#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_devices_grant_deviceId import Users_uId_devices_grant_deviceId
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_grant_deviceIdTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesgrantdeviceId = Users_uId_devices_grant_deviceId()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_grant_deviceId(self):
        u""""设备取消分享接口"""
        self.assertEqual(self.usersuIddevicesgrantdeviceId.users_uId_devices_grant_deviceId(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesgrantdeviceId= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_grant_deviceIdTestCase("test_users_uId_devices_grant_deviceId"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)