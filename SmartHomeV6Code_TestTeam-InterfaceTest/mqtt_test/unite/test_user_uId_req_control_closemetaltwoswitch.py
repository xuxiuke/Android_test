#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_closemetaltwoswitch import User_uId_req_control_closemetaltwoswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closemetaltwoswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosemetaltwoswitch = User_uId_req_control_closemetaltwoswitch()

    def test_user_uId_req_control_closemetaltwoswitch(self):
        u""""mqtt关闭金属二路开关"""
        self.assertEqual(self.useruIdreqcontrolclosemetaltwoswitch.user_uId_req_control_closemetaltwoswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closemetaltwoswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closemetaltwoswitchTestCase("test_user_uId_req_control_closemetaltwoswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)