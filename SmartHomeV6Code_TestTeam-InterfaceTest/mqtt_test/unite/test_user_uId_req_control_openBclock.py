#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_openBclock import User_uId_req_control_openBclock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openBclockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenBclock = User_uId_req_control_openBclock()

    def test_user_uId_req_control_openBclock(self):
        u""""mqtt打开Bc门锁"""
        self.assertEqual(self.useruIdreqcontrolopenBclock.user_uId_req_control_openBclock(),"0")

    def tearDown(self):
        self.user_uId_req_control_openBclock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openBclockTestCase("test_user_uId_req_control_openBclock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)