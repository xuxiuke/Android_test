#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closemetalthreeswitch import User_uId_req_control_closemetalthreeswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closemetalthreeswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosemetalthreeswitch = User_uId_req_control_closemetalthreeswitch()

    def test_user_uId_req_control_closemetalthreeswitch(self):
        u""""mqtt关闭金属三路开关"""
        self.assertEqual(self.useruIdreqcontrolclosemetalthreeswitch.user_uId_req_control_closemetalthreeswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closemetalthreeswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closemetalthreeswitchTestCase("test_user_uId_req_control_closemetalthreeswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)