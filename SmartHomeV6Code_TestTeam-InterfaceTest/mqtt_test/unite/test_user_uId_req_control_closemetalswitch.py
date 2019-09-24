#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closemetalswitch import User_uId_req_control_closemetalswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closemetalswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosemetalswitch = User_uId_req_control_closemetalswitch()

    def test_user_uId_req_control_closemetalswitch(self):
        u""""mqtt关闭金属一路开关"""
        self.assertEqual(self.useruIdreqcontrolclosemetalswitch.user_uId_req_control_closemetalswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closemetalswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closemetalswitchTestCase("test_user_uId_req_control_closemetalswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)