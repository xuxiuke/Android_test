#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openembeddedswitch_delay import User_uId_req_control_openembeddedswitch_delay
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openembeddedswitch_delayTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenembeddedswitch_delay = User_uId_req_control_openembeddedswitch_delay()

    def test_user_uId_req_control_openembeddedswitch_delay(self):
        u""""mqtt定时内嵌一路开关"""
        self.assertEqual(self.useruIdreqcontrolopenembeddedswitch_delay.user_uId_req_control_openembeddedswitch_delay(),"0")

    def tearDown(self):
        self.user_uId_req_control_openembeddedswitch_delay= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openembeddedswitch_delayTestCase("test_user_uId_req_control_openembeddedswitch_delay"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)