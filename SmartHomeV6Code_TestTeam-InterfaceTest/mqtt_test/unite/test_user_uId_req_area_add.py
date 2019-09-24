#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_area_add import User_uId_req_area_add
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_area_addTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqareaadd = User_uId_req_area_add()

    def test_user_uId_req_area_add(self):
        u""""mqtt新增理查test123区域"""
        self.assertEqual(self.useruIdreqareaadd.user_uId_req_area_add(),"0")

    def tearDown(self):
        self.user_uId_req_area_add= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_area_addTestCase("test_user_uId_req_area_add"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)