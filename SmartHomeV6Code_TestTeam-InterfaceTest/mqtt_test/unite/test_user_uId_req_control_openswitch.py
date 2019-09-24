#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openswitch import User_uId_req_control_openswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenswitch = User_uId_req_control_openswitch()

    def test_user_uId_req_control_openswitch(self):
        u""""mqtt打开单路开关"""
        self.assertEqual(self.useruIdreqcontrolopenswitch.user_uId_req_control_openswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openswitchTestCase("test_user_uId_req_control_openswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)