#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifywatersensorstatus import User_uId_req_modifywatersensorstatus
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifywatersensorstatusTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifywatersensorstatus = User_uId_req_modifywatersensorstatus()

    def test_user_uId_req_modifywatersensorstatus(self):
        u""""mqtt修改水浸为撤防状态"""
        self.assertEqual(self.useruIdreqmodifywatersensorstatus.user_uId_req_modifywatersensorstatus(),"0")

    def tearDown(self):
        self.user_uId_req_modifywatersensorstatus= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifywatersensorstatusTestCase("test_user_uId_req_modifywatersensorstatus"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)