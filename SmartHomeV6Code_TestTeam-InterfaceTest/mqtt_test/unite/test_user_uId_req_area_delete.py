#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_area_delete import User_uId_req_area_delete
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.public.user_uId_req_arealist import User_uId_req_arealist



class User_uId_req_area_deleteTestCase(unittest.TestCase):
    def setUp(self):
        arealist = User_uId_req_arealist()
        arealist.user_uId_req_arealist()
        self.useruIdreqareadelete = User_uId_req_area_delete()

    def test_user_uId_req_area_delete(self):
        u""""mqtt删除理查基娜test123区域"""
        self.assertEqual(self.useruIdreqareadelete.user_uId_req_area_delete(),"0")

    def tearDown(self):
        self.user_uId_req_area_modify= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_area_deleteTestCase("test_user_uId_req_area_delete"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)