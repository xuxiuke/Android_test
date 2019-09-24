#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_sense_switch import User_uId_req_sense_switch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_sense_switchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqsenseswitch = User_uId_req_sense_switch()

    def test_user_uId_req_sense_switch(self):
        u""""mqtt执行testing场景任务"""
        self.assertEqual(self.useruIdreqsenseswitch.user_uId_req_sense_switch(),"0")

    def tearDown(self):
        self.useruIdreqsenseswitch= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_sense_switchTestCase("test_user_uId_req_sense_switch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)