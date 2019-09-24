#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_closesocket import User_uId_req_control_closesocket
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closesocketTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosesocket = User_uId_req_control_closesocket()

    def test_user_uId_req_control_closesocket(self):
        u""""mqtt关闭墙面插座开关"""
        self.assertEqual(self.useruIdreqcontrolclosesocket.user_uId_req_control_closesocket(),"0")

    def tearDown(self):
        self.user_uId_req_control_closesocket= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closesocketTestCase("test_user_uId_req_control_closesocket"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
