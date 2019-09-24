#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.users_uId_third_devices import Users_uId_third_devices
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_third_devicesTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdthirddevices = Users_uId_third_devices()
        self.loginlogout = Login_logout()

    def test_users_uId_third_devices(self):
        u""""随便看1080p设备绑定"""
        self.assertEqual(self.usersuIdthirddevices.users_uId_third_devices(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdthirddevices = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_third_devicesTestCase("test_users_uId_third_devices"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)