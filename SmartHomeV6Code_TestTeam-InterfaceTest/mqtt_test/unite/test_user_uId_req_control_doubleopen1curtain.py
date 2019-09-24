#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_doubleopen1curtain import User_uId_req_control_doubleopen1curtain
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_doubleopen1curtainTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroldoubleopen1curtain = User_uId_req_control_doubleopen1curtain()

    def test_user_uId_req_control_doubleopen1curtain(self):
        u""""mqtt双路窗帘电机打开1窗帘"""
        self.assertEqual(self.useruIdreqcontroldoubleopen1curtain.user_uId_req_control_doubleopen1curtain(),"0")

    def tearDown(self):
        self.user_uId_req_control_doubleopen1curtain= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_doubleopen1curtainTestCase("test_user_uId_req_control_doubleopen1curtain"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)