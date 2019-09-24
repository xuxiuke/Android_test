#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closecurtains import User_uId_req_control_closecurtains
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closecurtainsTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosecurtains = User_uId_req_control_closecurtains()

    def test_user_uId_req_control_closecurtains(self):
        u""""mqtt暂停窗帘动作"""
        self.assertEqual(self.useruIdreqcontrolclosecurtains.user_uId_req_control_closecurtains(),"0")

    def tearDown(self):
        self.user_uId_req_control_closecurtains= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closecurtainsTestCase("test_user_uId_req_control_closecurtains"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
