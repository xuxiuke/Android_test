#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_devices_deviceId_bound import Users_uId_devices_deviceId_bound
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_devices_deviceId_boundTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesdeviceIdbound = Users_uId_devices_deviceId_bound()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_deviceId_bound(self):
        u""""获取绑定关系码,现用于爱看摄像头类设备"""
        self.assertEqual(self.usersuIddevicesdeviceIdbound.users_uId_devices_deviceId_bound(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesdeviceIdbound= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_deviceId_boundTestCase("test_users_uId_devices_deviceId_bound"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)