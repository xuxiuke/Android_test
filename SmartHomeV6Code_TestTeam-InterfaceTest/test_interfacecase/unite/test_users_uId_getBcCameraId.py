#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.users_uId_getBcCameraId import Users_uId_getBcCameraId
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Users_uId_getBcCameraIdTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIdgetBcCameraId = Users_uId_getBcCameraId()
        self.loginlogout = Login_logout()


    def test_users_uId_getBcCameraId(self):
        u""""查询Bc锁下的摄像机Id"""
        self.assertEqual(self.usersuIdgetBcCameraId.users_uId_getBcCameraId(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIdgetBcCameraId= None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_getBcCameraIdTestCase("test_users_uId_getBcCameraId"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)