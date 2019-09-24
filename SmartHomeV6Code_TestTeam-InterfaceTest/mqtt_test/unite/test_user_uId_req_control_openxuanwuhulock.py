#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openxuanwuhulock import User_uId_req_control_openxuanwuhulock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openxuanwuhulockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenxuanwuhulock = User_uId_req_control_openxuanwuhulock()

    def test_user_uId_req_control_openxuanwuhulock(self):
        u""""mqtt打开玄武湖门锁"""
        self.assertEqual(self.useruIdreqcontrolopenxuanwuhulock.user_uId_req_control_openxuanwuhulock(),"0")

    def tearDown(self):
        self.user_uId_req_control_openxuanwuhulock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openxuanwuhulockTestCase("test_user_uId_req_control_openxuanwuhulock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)