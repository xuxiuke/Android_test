#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closeembeddedswitch import User_uId_req_control_closeembeddedswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closeembeddedswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolcloseembeddedswitch = User_uId_req_control_closeembeddedswitch()

    def test_user_uId_req_control_closeembeddedswitch(self):
        u""""mqtt关闭内嵌一路开关"""
        self.assertEqual(self.useruIdreqcontrolcloseembeddedswitch.user_uId_req_control_closeembeddedswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_closeembeddedswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closeembeddedswitchTestCase("test_user_uId_req_control_closeembeddedswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)