#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.users_uId_devices_resource_token import Users_uId_devices_resource_token
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_devices_resource_tokenTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIddevicesresourcetoken = Users_uId_devices_resource_token()
        self.loginlogout = Login_logout()

    def test_users_uId_devices_resource_token(self):
        u"""获取阿里访问资源的秘钥"""
        self.assertEqual(self.usersuIddevicesresourcetoken.users_uId_devices_resource_token(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIddevicesresourcetoken = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_devices_resource_tokenTestCase("test_users_uId_devices_resource_token"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)