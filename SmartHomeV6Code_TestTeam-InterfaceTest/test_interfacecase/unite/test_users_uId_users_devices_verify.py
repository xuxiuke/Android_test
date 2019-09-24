#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.users_uId_users_devices_verify import Users_uId_users_devices_verify
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_users_devices_verifyTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdusersdevicesverify = Users_uId_users_devices_verify()
        self.loginlogout = Login_logout()

    def test_users_uId_users_devices_verify(self):
        u""""查询账号和摄像头设备绑定关系"""
        self.assertEqual(self.usersuIdusersdevicesverify.users_uId_users_devices_verify(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdusersdevicesverify = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_users_devices_verifyTestCase("test_users_uId_users_devices_verify"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)