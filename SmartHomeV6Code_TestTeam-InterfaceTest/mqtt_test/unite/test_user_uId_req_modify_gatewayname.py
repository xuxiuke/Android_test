#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_modify_gatewayname import User_uId_req_modify_gatewayname
from mqtt_test.mqtt_bussiness import global_value




class User_uId_req_modify_gatewaynameTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifygatewayname = User_uId_req_modify_gatewayname()


    def test_user_uId_req_modify_gatewayname(self):
        u""""mqtt修改网关的名称"""
        self.assertEqual(self.useruIdreqmodifygatewayname.user_uId_req_modify_gatewayname(),"0")

    def tearDown(self):
        self.user_uId_req_modify_gatewayname= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modify_gatewaynameTestCase("test_user_uId_req_modify_gatewayname"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)

