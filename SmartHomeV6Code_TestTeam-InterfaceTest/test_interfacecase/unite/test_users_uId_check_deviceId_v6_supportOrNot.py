#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_check_deviceId_v6_supportOrNot import Users_uId_check_deviceId_v6_supportOrNot
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_check_deviceId_v6_supportOrNotTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdcheckdeviceIdv6supportOrNot = Users_uId_check_deviceId_v6_supportOrNot()
        self.loginlogout = Login_logout()

    def test_users_uId_check_deviceId_v6_supportOrNot(self):
        u""""校验设备是否是v6支持"""
        self.assertEqual(self.usersuIdcheckdeviceIdv6supportOrNot.users_uId_check_deviceId_v6_supportOrNot(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdcheckdeviceIdv6supportOrNot = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_check_deviceId_v6_supportOrNotTestCase("test_users_uId_check_deviceId_v6_supportOrNot"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)

