#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_deleteAlarmInfo import Users_uId_devices_deleteAlarmInfo
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_deleteAlarmInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesdeleteAlarmInfo = Users_uId_devices_deleteAlarmInfo()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_deleteAlarmInfo(self):
        u""""删除用户消息中心报警消息"""
        self.assertEqual(self.usersuIddevicesdeleteAlarmInfo.users_uId_devices_deleteAlarmInfo(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesdeleteAlarmInfo = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_deleteAlarmInfoTestCase("test_users_uId_devices_deleteAlarmInfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)