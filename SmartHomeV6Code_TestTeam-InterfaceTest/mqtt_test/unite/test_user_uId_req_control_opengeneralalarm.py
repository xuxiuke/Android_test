#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_opengeneralalarm import User_uId_req_control_opengeneralalarm
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_opengeneralalarmTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopengeneralalarm = User_uId_req_control_opengeneralalarm()

    def test_user_uId_req_control_opengeneralalarm(self):
        u""""mqtt打开通用报警"""
        self.assertEqual(self.useruIdreqcontrolopengeneralalarm.user_uId_req_control_opengeneralalarm(),"0")

    def tearDown(self):
        self.user_uId_req_control_opengeneralalarm= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_opengeneralalarmTestCase("test_user_uId_req_control_opengeneralalarm"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)