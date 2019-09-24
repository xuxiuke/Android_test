#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_closeDINswitch import User_uId_req_control_closeDINswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closeDINswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolcloseDINswitch = User_uId_req_control_closeDINswitch()

    def test_user_uId_req_control_closeDINswitch(self):
        u""""mqtt关闭DIN计量开关"""
        self.assertEqual(self.useruIdreqcontrolcloseDINswitch.user_uId_req_control_closeDINswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closeDINswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closeDINswitchTestCase("test_user_uId_req_control_closeDINswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)