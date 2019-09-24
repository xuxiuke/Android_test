#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_senselist import User_uId_req_senselist
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_senselistTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqsenselist = User_uId_req_senselist()


    def test_user_uId_req_senselist(self):
        u""""mqtt查询场景列表"""
        self.assertEqual(self.useruIdreqsenselist.user_uId_req_senselist(),"0")

    def tearDown(self):
        self.useruIdreqsenselist= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_senselistTestCase("test_user_uId_req_senselist"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)