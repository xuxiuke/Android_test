#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_alarm_Details import Users_uId_devices_alarm_Details
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_alarm_DetailsTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesalarmDetails = Users_uId_devices_alarm_Details()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_alarm_Details(self):
        u""""随便看--告警相关"""
        self.assertEqual(self.usersuIddevicesalarmDetails.users_uId_devices_alarm_Details(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesalarmDetails = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_alarm_DetailsTestCase("test_users_uId_devices_alarm_Details"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)