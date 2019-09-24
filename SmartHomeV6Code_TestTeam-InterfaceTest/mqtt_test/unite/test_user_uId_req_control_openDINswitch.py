#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openDINswitch import User_uId_req_control_openDINswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openDINswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenDINswitch = User_uId_req_control_openDINswitch()

    def test_user_uId_req_control_openDINswitch(self):
        u""""mqtt打开DIN计量开关"""
        self.assertEqual(self.useruIdreqcontrolopenDINswitch.user_uId_req_control_openDINswitch(),"0")

    def tearDown(self):
        self.user_uId_req_control_openDINswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openDINswitchTestCase("test_user_uId_req_control_openDINswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
