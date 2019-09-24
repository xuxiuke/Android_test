#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_arealist import User_uId_req_arealist
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_arealistTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqarealist = User_uId_req_arealist()

    def test_user_uId_req_arealist(self):
        u""""mqtt刷新区域列表"""
        self.assertEqual(self.useruIdreqarealist.user_uId_req_arealist(),"0")

    def tearDown(self):
        self.user_uId_req_arealist= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_arealistTestCase("test_user_uId_req_arealist"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)