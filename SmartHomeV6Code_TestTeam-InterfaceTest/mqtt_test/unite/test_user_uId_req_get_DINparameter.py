#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_get_DINparameter import User_uId_req_get_DINparameter
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_get_DINparameterTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqgetDINparameter = User_uId_req_get_DINparameter()


    def test_user_uId_req_get_DINparameter(self):
        u""""mqtt获取DIN参数"""
        self.assertEqual(self.useruIdreqgetDINparameter.user_uId_req_get_DINparameter(),"0")

    def tearDown(self):
        self.useruIdreqgetDINparameter= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_get_DINparameterTestCase("test_user_uId_req_get_DINparameter"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)