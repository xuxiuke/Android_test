#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closetwoswitch import User_uId_req_control_closetwoswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closetwoswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosetwoswitch = User_uId_req_control_closetwoswitch()

    def test_user_uId_req_control_closetwoswitch(self):
        u""""mqtt关闭二路开关的第一路"""
        self.assertEqual(self.useruIdreqcontrolclosetwoswitch.user_uId_req_control_closetwoswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closetwoswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closetwoswitchTestCase("test_user_uId_req_control_closetwoswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)