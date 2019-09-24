#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_touchdimmingswitch import User_uId_req_control_touchdimmingswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_touchdimmingswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroltouchdimmingswitch = User_uId_req_control_touchdimmingswitch()

    def test_user_uId_req_control_touchdimmingswitch(self):
        u""""mqtt调整触摸调光开关亮度变亮"""
        self.assertEqual(self.useruIdreqcontroltouchdimmingswitch.user_uId_req_control_touchdimmingswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_touchdimmingswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_touchdimmingswitchTestCase("test_user_uId_req_control_touchdimmingswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)