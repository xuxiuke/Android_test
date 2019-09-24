#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_openmobilesocket import User_uId_req_control_openmobilesocket
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openmobilesocketTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenmobilesocket = User_uId_req_control_openmobilesocket()

    def test_user_uId_req_control_openmobilesocket(self):
        u""""mqtt打开移动计量插座开关"""
        self.assertEqual(self.useruIdreqcontrolopenmobilesocket.user_uId_req_control_openmobilesocket(),"0")

    def tearDown(self):
        self.user_uId_req_control_openmobilesocket= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openmobilesocketTestCase("test_user_uId_req_control_openmobilesocket"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)