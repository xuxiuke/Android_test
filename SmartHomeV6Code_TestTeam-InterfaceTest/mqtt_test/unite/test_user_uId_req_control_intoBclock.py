#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_intoBclock import User_uId_req_control_intoBclock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_intoBclockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolintoBclock = User_uId_req_control_intoBclock()

    def test_user_uId_req_control_intoBclock(self):
        u""""mqtt进入Bc锁主页面"""
        self.assertEqual(self.useruIdreqcontrolintoBclock.user_uId_req_control_intoBclock(),"0")

    def tearDown(self):
        self.user_uId_req_control_intoBclock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_intoBclockTestCase("test_user_uId_req_control_intoBclock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)