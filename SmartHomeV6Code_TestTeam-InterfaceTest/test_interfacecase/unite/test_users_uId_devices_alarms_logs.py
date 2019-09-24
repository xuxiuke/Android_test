#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_alarms_logs import Users_uId_devices_alarms_logs
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_alarms_logsTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesalarmslogs = Users_uId_devices_alarms_logs()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_alarms_logs(self):
        u""""获取用户网关下子设备log未读数（红外入侵）"""
        self.assertEqual(self.usersuIddevicesalarmslogs.users_uId_devices_alarms_logs(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesalarmslogs = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_alarms_logsTestCase("test_users_uId_devices_alarms_logs"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)