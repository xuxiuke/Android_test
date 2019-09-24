#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_close_steward import User_uId_req_close_steward
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.public.user_uId_req_stewardlist import User_uId_req_stewardlist



class User_uId_req_close_stewardTestCase(unittest.TestCase):
    def setUp(self):
        new = User_uId_req_stewardlist()
        new.user_uId_req_stewardlist()
        self.useruIdreqclosesteward = User_uId_req_close_steward()
        #print("need is", global_value.get_return_programID_value())

    def test_user_uId_req_close_steward(self):
        u""""mqtt关闭打开开关管家"""
        self.assertEqual(self.useruIdreqclosesteward.user_uId_req_close_steward(),"0")

    def tearDown(self):
        self.user_uId_req_close_steward= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_close_stewardTestCase("test_user_uId_req_close_steward"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)