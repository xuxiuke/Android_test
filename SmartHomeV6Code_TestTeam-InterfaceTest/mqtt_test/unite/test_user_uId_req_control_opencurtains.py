#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_opencurtains import User_uId_req_control_opencurtains
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_opencurtainsTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopencurtains = User_uId_req_control_opencurtains()

    def test_user_uId_req_control_opencurtains(self):
        u""""mqtt打开窗帘点击开关"""
        self.assertEqual(self.useruIdreqcontrolopencurtains.user_uId_req_control_opencurtains(),"0")

    def tearDown(self):
        self.user_uId_req_control_opencurtains= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_opencurtainsTestCase("test_user_uId_req_control_opencurtains"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
