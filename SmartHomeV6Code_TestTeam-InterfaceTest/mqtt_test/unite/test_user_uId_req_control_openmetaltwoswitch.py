#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openmetaltwoswitch import User_uId_req_control_openmetaltwoswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openmetaltwoswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenmetaltwoswitch = User_uId_req_control_openmetaltwoswitch()

    def test_user_uId_req_control_openmetaltwoswitch(self):
        u""""mqtt打开金属二路开关"""
        self.assertEqual(self.useruIdreqcontrolopenmetaltwoswitch.user_uId_req_control_openmetaltwoswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openmetaltwoswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openmetaltwoswitchTestCase("test_user_uId_req_control_openmetaltwoswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)