#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



import unittest
from mqtt_test.public.user_uId_req_control_openmetalthreeswitch import User_uId_req_control_openmetalthreeswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openmetalthreeswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenmetalthreeswitch = User_uId_req_control_openmetalthreeswitch()

    def test_user_uId_req_control_openmetalthreeswitch(self):
        u""""mqtt打开金属三路开关"""
        self.assertEqual(self.useruIdreqcontrolopenmetalthreeswitch.user_uId_req_control_openmetalthreeswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openmetalthreeswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openmetalthreeswitchTestCase("test_user_uId_req_control_openmetalthreeswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)