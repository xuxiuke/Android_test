#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closeswitch import User_uId_req_control_closeswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closeswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolcloseswitch = User_uId_req_control_closeswitch()

    def test_user_uId_req_control_closeswitch(self):
        u""""mqtt关闭单路开关"""
        self.assertEqual(self.useruIdreqcontrolcloseswitch.user_uId_req_control_closeswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closeswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closeswitchTestCase("test_user_uId_req_control_closeswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)