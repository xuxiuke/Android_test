#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



import unittest
from mqtt_test.public.user_uId_req_forbiddoorbellacoustooptic import User_uId_req_forbiddoorbellacoustooptic
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_forbiddoorbellacoustoopticTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqforbiddoorbellacoustooptic = User_uId_req_forbiddoorbellacoustooptic()

    def test_user_uId_req_forbiddoorbellacoustooptic(self):
        u""""mqtt门铃声光器禁止门铃按钮进行联动"""
        self.assertEqual(self.useruIdreqforbiddoorbellacoustooptic.user_uId_req_forbiddoorbellacoustooptic(),"0")

    def tearDown(self):
        self.user_uId_req_forbiddoorbellacoustooptic= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_forbiddoorbellacoustoopticTestCase("test_user_uId_req_forbiddoorbellacoustooptic"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)