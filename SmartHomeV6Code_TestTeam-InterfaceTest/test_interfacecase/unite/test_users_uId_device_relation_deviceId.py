#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_device_relation_deviceId import Users_uId_device_relation_deviceId
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_device_relation_deviceIdTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicerelationdeviceId = Users_uId_device_relation_deviceId()
        self.loginlogout = Login_logout()


    def test_users_uId_device_relation_deviceId(self):
        u""""查询设备间关系"""
        self.assertEqual(self.usersuIddevicerelationdeviceId.users_uId_device_relation_deviceId(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicerelationdeviceId= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_device_relation_deviceIdTestCase("test_users_uId_device_relation_deviceId"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)