#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_delayopenDINswitch import User_uId_req_control_delayopenDINswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_delayopenDINswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontroldelayopenDINswitch = User_uId_req_control_delayopenDINswitch()

    def test_user_uId_req_control_delayopenDINswitch(self):
        u""""mqtt延时打开DIN计量开关"""
        self.assertEqual(self.useruIdreqcontroldelayopenDINswitch.user_uId_req_control_delayopenDINswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_delayopenDINswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_delayopenDINswitchTestCase("test_user_uId_req_control_delayopenDINswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)