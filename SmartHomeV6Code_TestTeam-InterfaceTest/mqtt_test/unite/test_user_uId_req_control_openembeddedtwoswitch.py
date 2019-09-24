#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openembeddedtwoswitch import User_uId_req_control_openembeddedtwoswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openembeddedtwoswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenembeddedtwoswitch = User_uId_req_control_openembeddedtwoswitch()

    def test_user_uId_req_control_openembeddedtwoswitch(self):
        u""""mqtt打开内嵌二路开关"""
        self.assertEqual(self.useruIdreqcontrolopenembeddedtwoswitch.user_uId_req_control_openembeddedtwoswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openembeddedtwoswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openembeddedtwoswitchTestCase("test_user_uId_req_control_openembeddedtwoswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)