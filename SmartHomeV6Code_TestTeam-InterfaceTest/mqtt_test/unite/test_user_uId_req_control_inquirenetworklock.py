#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_inquirenetworklock import User_uId_req_control_inquirenetworklock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_inquirenetworklockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolinquirenetworklock = User_uId_req_control_inquirenetworklock()

    def test_user_uId_req_control_inquirenetworklock(self):
        u""""mqtt查询网络锁状态"""
        self.assertEqual(self.useruIdreqcontrolinquirenetworklock.user_uId_req_control_inquirenetworklock(),"0")

    def tearDown(self):
        self.user_uId_req_control_inquirenetworklock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_inquirenetworklockTestCase("test_user_uId_req_control_inquirenetworklock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)