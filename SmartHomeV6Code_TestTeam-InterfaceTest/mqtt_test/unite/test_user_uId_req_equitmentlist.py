#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_equitmentlist import User_uId_req_equitmentlist
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_equitmentlistTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqequitmentlist = User_uId_req_equitmentlist()


    def test_user_uId_req_equitmentlist(self):
        u""""mqtt查询设备列表"""
        self.assertEqual(self.useruIdreqequitmentlist.user_uId_req_equitmentlist(),"0")

    def tearDown(self):
        self.useruIdreqequitmentlist= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_equitmentlistTestCase("test_user_uId_req_equitmentlist"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)