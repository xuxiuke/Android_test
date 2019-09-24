#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_device_relation_deviceId_delete import Users_uId_device_relation_deviceId_delete
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_device_relation_deviceId_deleteTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicerelationdeviceIddelete = Users_uId_device_relation_deviceId_delete()
        self.loginlogout = Login_logout()


    def test_users_uId_device_relation_deviceId_delete(self):
        u""""删除设备间关系"""
        self.assertEqual(self.usersuIddevicerelationdeviceIddelete.users_uId_device_relation_deviceId_delete(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicerelationdeviceIddelete= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_device_relation_deviceId_deleteTestCase("test_users_uId_device_relation_deviceId_delete"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)