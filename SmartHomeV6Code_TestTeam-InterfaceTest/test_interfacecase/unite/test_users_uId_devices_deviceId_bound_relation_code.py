#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_devices_deviceId_bound_relation_code import Users_uId_devices_deviceId_bound_relation_code
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_deviceId_bound_relation_codeTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesdeviceIdboundrelation_code = Users_uId_devices_deviceId_bound_relation_code()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_deviceId_bound_relation_code(self):
        u""""获取绑定关系码,现用于爱看摄像头类设备"""
        self.assertEqual(self.usersuIddevicesdeviceIdboundrelation_code.users_uId_devices_deviceId_bound_relation_code(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesdeviceIdboundrelation_code= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_deviceId_bound_relation_codeTestCase("test_users_uId_devices_deviceId_bound_relation_code"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)