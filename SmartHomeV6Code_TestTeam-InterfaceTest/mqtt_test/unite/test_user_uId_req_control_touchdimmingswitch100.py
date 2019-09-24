#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_touchdimmingswitch100 import User_uId_req_control_touchdimmingswitch100
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_touchdimmingswitch100TestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroltouchdimmingswitch100 = User_uId_req_control_touchdimmingswitch100()

    def test_user_uId_req_control_touchdimmingswitch100(self):
        u""""mqtt调整触摸调光开关亮度变亮100"""
        self.assertEqual(self.useruIdreqcontroltouchdimmingswitch100.user_uId_req_control_touchdimmingswitch100(),"0")

    def tearDown(self):
        self.user_uId_req_control_touchdimmingswitch100= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_touchdimmingswitch100TestCase("test_user_uId_req_control_touchdimmingswitch100"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)