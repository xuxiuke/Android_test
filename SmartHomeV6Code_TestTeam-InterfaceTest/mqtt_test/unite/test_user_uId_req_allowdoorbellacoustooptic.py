#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



import unittest
from mqtt_test.public.user_uId_req_allowdoorbellacoustooptic import User_uId_req_allowdoorbellacoustooptic
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_allowdoorbellacoustoopticTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqallowdoorbellacoustooptic = User_uId_req_allowdoorbellacoustooptic()

    def test_user_uId_req_allowdoorbellacoustooptic(self):
        u""""mqtt门铃声光器允许门铃按钮进行联动"""
        self.assertEqual(self.useruIdreqallowdoorbellacoustooptic.user_uId_req_allowdoorbellacoustooptic(),"0")

    def tearDown(self):
        self.user_uId_req_allowdoorbellacoustooptic= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_allowdoorbellacoustoopticTestCase("test_user_uId_req_allowdoorbellacoustooptic"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)