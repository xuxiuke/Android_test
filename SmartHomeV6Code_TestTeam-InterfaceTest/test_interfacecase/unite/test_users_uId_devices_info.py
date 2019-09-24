#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_devices_info import Users_uId_devices_info
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesinfo = Users_uId_devices_info()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_info(self):
        u"""修改设备信息"""
        self.assertEqual(self.usersuIddevicesinfo.users_uId_devices_info(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesinfo = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_infoTestCase("test_users_uId_devices_info"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)