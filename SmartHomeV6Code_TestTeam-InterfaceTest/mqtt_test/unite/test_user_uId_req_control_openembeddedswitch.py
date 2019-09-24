#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openembeddedswitch import User_uId_req_control_openembeddedswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openembeddedswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenembeddedswitch = User_uId_req_control_openembeddedswitch()

    def test_user_uId_req_control_openembeddedswitch(self):
        u""""mqtt打开内嵌一路开关"""
        self.assertEqual(self.useruIdreqcontrolopenembeddedswitch.user_uId_req_control_openembeddedswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openembeddedswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openembeddedswitchTestCase("test_user_uId_req_control_openembeddedswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)