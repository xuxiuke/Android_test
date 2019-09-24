#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_creat_steward import User_uId_req_creat_steward
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_creat_stewardTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcreatsteward = User_uId_req_creat_steward()

    def test_user_uId_req_creat_steward(self):
        u""""mqtt创建定时管家"""
        self.assertEqual(self.useruIdreqcreatsteward.user_uId_req_creat_steward(),"0")

    def tearDown(self):
        self.user_uId_req_creat_steward= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_creat_stewardTestCase("test_user_uId_req_creat_steward"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)