#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_check_deviceId_v6_supportOrNot_non import Users_uId_check_deviceId_v6_supportOrNot_non
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_check_deviceId_v6_supportOrNot_nonTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdcheckdeviceIdv6supportOrNotnon = Users_uId_check_deviceId_v6_supportOrNot_non()
        self.loginlogout = Login_logout()

    def test_users_uId_check_deviceId_v6_supportOrNot_non(self):
        u""""校验设备是否是v6支持"""
        self.assertEqual(self.usersuIdcheckdeviceIdv6supportOrNotnon.users_uId_check_deviceId_v6_supportOrNot_non(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdcheckdeviceIdv6supportOrNotnon = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_check_deviceId_v6_supportOrNot_nonTestCase("test_users_uId_check_deviceId_v6_supportOrNot_non"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
