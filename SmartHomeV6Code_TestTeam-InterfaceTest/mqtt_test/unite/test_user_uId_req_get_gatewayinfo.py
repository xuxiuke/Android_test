#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_get_gatewayinfo import User_uId_req_get_gatewayinfo
from mqtt_test.mqtt_bussiness import global_value


class User_uId_req_get_gatewayinfoTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqgetgatewayinfo = User_uId_req_get_gatewayinfo()


    def test_user_uId_req_get_gatewayinfo(self):
        u""""mqtt查询网关信息"""
        self.assertEqual(self.useruIdreqgetgatewayinfo.user_uId_req_get_gatewayinfo(),"0")

    def tearDown(self):
        self.useruIdreqgetgatewayinfo= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_get_gatewayinfoTestCase("test_user_uId_req_get_gatewayinfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)