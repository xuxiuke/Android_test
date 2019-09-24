#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_stopcurtains import User_uId_req_control_stopcurtains
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_stopcurtainsTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolstopcurtains = User_uId_req_control_stopcurtains()

    def test_user_uId_req_control_stopcurtains(self):
        u""""mqtt暂停窗帘动作"""
        self.assertEqual(self.useruIdreqcontrolstopcurtains.user_uId_req_control_stopcurtains(),"0")

    def tearDown(self):
        self.user_uId_req_control_stopcurtains= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_stopcurtainsTestCase("test_user_uId_req_control_stopcurtains"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)