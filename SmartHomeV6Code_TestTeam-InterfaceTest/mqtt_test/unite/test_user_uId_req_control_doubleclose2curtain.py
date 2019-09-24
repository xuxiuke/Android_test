#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_doubleclose2curtain import User_uId_req_control_doubleclose2curtain
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_doubleclose2curtainTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroldoubleclose2curtain = User_uId_req_control_doubleclose2curtain()

    def test_user_uId_req_control_doubleclose2curtain(self):
        u""""mqtt双路窗帘电机关闭2窗帘"""
        self.assertEqual(self.useruIdreqcontroldoubleclose2curtain.user_uId_req_control_doubleclose2curtain(),"0")

    def tearDown(self):
        self.user_uId_req_control_doubleclose2curtain= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_doubleclose2curtainTestCase("test_user_uId_req_control_doubleclose2curtain"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)