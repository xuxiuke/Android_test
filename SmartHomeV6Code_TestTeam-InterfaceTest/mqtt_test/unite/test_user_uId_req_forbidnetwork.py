#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_forbidnetwork import User_uId_req_forbidnetwork
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_forbidnetworkTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqforbidnetwork = User_uId_req_forbidnetwork()

    def test_user_uId_req_forbidnetwork(self):
        u""""mqtt禁止添加网络"""
        self.assertEqual(self.useruIdreqforbidnetwork.user_uId_req_forbidnetwork(),"0")

    def tearDown(self):
        self.user_uId_req_forbidnetwork= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_forbidnetworkTestCase("test_user_uId_req_forbidnetwork"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)