#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openpasswordlock import User_uId_req_control_openpasswordlock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openpasswordlockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenpasswordlock = User_uId_req_control_openpasswordlock()

    def test_user_uId_req_control_openpasswordlock(self):
        u""""mqtt打开密码门锁"""
        self.assertEqual(self.useruIdreqcontrolopenpasswordlock.user_uId_req_control_openpasswordlock(),"0")

    def tearDown(self):
        self.user_uId_req_control_openpasswordlock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openpasswordlockTestCase("test_user_uId_req_control_openpasswordlock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)