#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_networklockbindsense import User_uId_req_control_networklockbindsense
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_networklockbindsenseTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolnetworklockbindsense = User_uId_req_control_networklockbindsense()

    def test_user_uId_req_control_networklockbindsense(self):
        u""""mqtt网络锁绑定场景"""
        self.assertEqual(self.useruIdreqcontrolnetworklockbindsense.user_uId_req_control_networklockbindsense(),"0")

    def tearDown(self):
        self.user_uId_req_control_networklockbindsense= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_networklockbindsenseTestCase("test_user_uId_req_control_networklockbindsense"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)