#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_devices_deviceId_getChildDevices import Users_uId_devices_deviceId_getChildDevices
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout



class Users_uId_devices_deviceId_getChildDevicesTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesdeviceIdgetChildDevices = Users_uId_devices_deviceId_getChildDevices()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_deviceId_getChildDevices(self):
        u""""获取顶级设备下的子设备信息"""
        self.assertEqual(self.usersuIddevicesdeviceIdgetChildDevices.users_uId_devices_deviceId_getChildDevices(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesdeviceIdgetChildDevices= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_deviceId_getChildDevicesTestCase("test_users_uId_devices_deviceId_getChildDevices"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)