#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_devices_staticInfo import Users_uId_devices_staticInfo
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_devices_staticInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesstaticInfo = Users_uId_devices_staticInfo()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_staticInfo(self):
        u""""获取设备静态信息"""
        self.assertEqual(self.usersuIddevicesstaticInfo.users_uId_devices_staticInfo(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesstaticInfo= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_staticInfoTestCase("test_users_uId_devices_staticInfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)