#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_closefire import User_uId_req_control_closefire
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closefireTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosefire = User_uId_req_control_closefire()

    def test_user_uId_req_control_closefire(self):
        u""""mqtt关闭火警开关"""
        self.assertEqual(self.useruIdreqcontrolclosefire.user_uId_req_control_closefire(),"0")

    def tearDown(self):
        self.user_uId_req_control_closefire= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closefireTestCase("test_user_uId_req_control_closefire"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)