#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_allownetwork import User_uId_req_allownetwork
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_allownetworkTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqallownetwork = User_uId_req_allownetwork()

    def test_user_uId_req_allownetwork(self):
        u""""mqtt永久开启允许添加网络"""
        self.assertEqual(self.useruIdreqallownetwork.user_uId_req_allownetwork(),"0")

    def tearDown(self):
        self.user_uId_req_allownetwork= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_allownetworkTestCase("test_user_uId_req_allownetwork"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)