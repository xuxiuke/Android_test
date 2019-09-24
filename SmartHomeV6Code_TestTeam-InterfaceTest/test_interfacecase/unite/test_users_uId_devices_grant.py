#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from  test_interfacecase.public.users_uId_devices_grant import Users_uId_devices_grant
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_grantTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesgrant = Users_uId_devices_grant()
        self.loginlogout = Login_logout()


    def test_users_uId_devices_grant(self):
        u""""设备分享"""
        self.assertEqual(self.usersuIddevicesgrant.users_uId_devices_grant(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesgrant= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_grantTestCase("test_users_uId_devices_grant"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)