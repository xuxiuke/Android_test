#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_networklockunbindsense import User_uId_req_control_networklockunbindsense
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_networklockunbindsenseTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolnetworklockunbindsense = User_uId_req_control_networklockunbindsense()

    def test_user_uId_req_control_networklockunbindsense(self):
        u""""mqtt网络锁绑定场景"""
        self.assertEqual(self.useruIdreqcontrolnetworklockunbindsense.user_uId_req_control_networklockunbindsense(),"0")

    def tearDown(self):
        self.user_uId_req_control_networklockunbindsense= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_networklockunbindsenseTestCase("test_user_uId_req_control_networklockunbindsense"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)