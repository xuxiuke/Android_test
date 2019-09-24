#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openmetalswitch import User_uId_req_control_openmetalswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openmetalswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenmetalswitch = User_uId_req_control_openmetalswitch()

    def test_user_uId_req_control_openmetalswitch(self):
        u""""mqtt打开金属一路开关"""
        self.assertEqual(self.useruIdreqcontrolopenmetalswitch.user_uId_req_control_openmetalswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openmetalswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openmetalswitchTestCase("test_user_uId_req_control_openmetalswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)