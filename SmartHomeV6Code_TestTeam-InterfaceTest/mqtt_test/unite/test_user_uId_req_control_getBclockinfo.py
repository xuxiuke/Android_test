#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_getBclockinfo import User_uId_req_control_getBclockinfo
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_getBclockinfoTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolgetBclockinfo = User_uId_req_control_getBclockinfo()

    def test_user_uId_req_control_getBclockinfo(self):
        u""""mqtt查询Bc锁信息"""
        self.assertEqual(self.useruIdreqcontrolgetBclockinfo.user_uId_req_control_getBclockinfo(),"0")

    def tearDown(self):
        self.user_uId_req_control_getBclockinfo= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_getBclockinfoTestCase("test_user_uId_req_control_getBclockinfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)