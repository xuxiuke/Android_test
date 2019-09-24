#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closeembeddedtwoswitch import User_uId_req_control_closeembeddedtwoswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closeembeddedtwoswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolcloseembeddedtwoswitch = User_uId_req_control_closeembeddedtwoswitch()

    def test_user_uId_req_control_closeembeddedtwoswitch(self):
        u""""mqtt关闭内嵌二路开关"""
        self.assertEqual(self.useruIdreqcontrolcloseembeddedtwoswitch.user_uId_req_control_closeembeddedtwoswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closeembeddedtwoswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closeembeddedtwoswitchTestCase("test_user_uId_req_control_closeembeddedtwoswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)