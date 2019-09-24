#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from  test_interfacecase.public.users_uId_devices_grant_deviceId_granteeUid import Users_uId_devices_grant_deviceId_granteeUid
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_devices_grant_deviceId_granteeUidTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesgrantdeviceIdgranteeUid = Users_uId_devices_grant_deviceId_granteeUid()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_grant_deviceId_granteeUid(self):
        u""""取消设备分享"""
        self.assertEqual(self.usersuIddevicesgrantdeviceIdgranteeUid.users_uId_devices_grant_deviceId_granteeUid(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesgrantdeviceIdgranteeUid= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_grant_deviceId_granteeUidTestCase("test_users_uId_devices_grant_deviceId_granteeUid"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)