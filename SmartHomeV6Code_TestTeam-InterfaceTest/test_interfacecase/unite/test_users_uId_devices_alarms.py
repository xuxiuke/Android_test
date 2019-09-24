#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_alarms import Users_uId_devices_alarms
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_alarmsTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesalarms = Users_uId_devices_alarms()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_alarms(self):
        u""""获取用户网关下子设备告警未读数（红外入侵）"""
        self.assertEqual(self.usersuIddevicesalarms.users_uId_devices_alarms(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesalarms = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_alarmsTestCase("test_users_uId_devices_alarms"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)