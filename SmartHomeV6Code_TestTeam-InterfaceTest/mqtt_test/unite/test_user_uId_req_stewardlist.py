#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_stewardlist import User_uId_req_stewardlist
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_stewardlistTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqstewardlist = User_uId_req_stewardlist()


    def test_user_uId_req_stewardlist(self):
        u""""mqtt查询管家列表"""
        self.assertEqual(self.useruIdreqstewardlist.user_uId_req_stewardlist(),"0")

    def tearDown(self):
        self.useruIdreqstewardlist= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_stewardlistTestCase("test_user_uId_req_stewardlist"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)