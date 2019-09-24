#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_opennetworklock import User_uId_req_control_opennetworklock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_opennetworklockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopennetworklock = User_uId_req_control_opennetworklock()

    def test_user_uId_req_control_opennetworklock(self):
        u""""mqtt打开网络锁门锁"""
        self.assertEqual(self.useruIdreqcontrolopennetworklock.user_uId_req_control_opennetworklock(),"0")

    def tearDown(self):
        self.user_uId_req_control_opennetworklock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_opennetworklockTestCase("test_user_uId_req_control_opennetworklock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)