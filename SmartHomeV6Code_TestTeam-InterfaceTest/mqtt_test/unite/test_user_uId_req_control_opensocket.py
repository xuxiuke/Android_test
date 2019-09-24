#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_opensocket import User_uId_req_control_opensocket
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_opensocketTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopensocket = User_uId_req_control_opensocket()

    def test_user_uId_req_control_opensocket(self):
        u""""mqtt打开墙面插座开关"""
        self.assertEqual(self.useruIdreqcontrolopensocket.user_uId_req_control_opensocket(),"0")

    def tearDown(self):
        self.user_uId_req_control_opensocket= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_opensocketTestCase("test_user_uId_req_control_opensocket"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
