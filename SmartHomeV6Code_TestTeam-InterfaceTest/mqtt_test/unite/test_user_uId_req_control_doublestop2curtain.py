#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_doublestop2curtain import User_uId_req_control_doublestop2curtain
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_doublestop2curtainTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroldoublestop2curtain = User_uId_req_control_doublestop2curtain()

    def test_user_uId_req_control_doublestop2curtain(self):
        u""""mqtt双路窗帘电机停止2窗帘"""
        self.assertEqual(self.useruIdreqcontroldoublestop2curtain.user_uId_req_control_doublestop2curtain(),"0")

    def tearDown(self):
        self.user_uId_req_control_doublestop2curtain= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_doublestop2curtainTestCase("test_user_uId_req_control_doublestop2curtain"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)