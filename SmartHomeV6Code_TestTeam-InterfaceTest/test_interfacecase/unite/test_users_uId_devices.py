#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from test_interfacecase.public.users_uId_devices import Users_uId_devices
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_devicesTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevices = Users_uId_devices()
        self.loginlogout = Login_logout()


    def test_users_uId_devices(self):
        u""""获取sip信息,现用于爱看摄像头类设备"""
        self.assertEqual(self.usersuIddevices.users_uId_devices(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevices= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devicesTestCase("test_users_uId_devices"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)