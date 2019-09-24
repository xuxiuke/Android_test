#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_closemobilesocket import User_uId_req_control_closemobilesocket
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_closemobilesocketTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolclosemobilesocket = User_uId_req_control_closemobilesocket()

    def test_user_uId_req_control_closemobilesocket(self):
        u""""mqtt关闭移动计量插座开关"""
        self.assertEqual(self.useruIdreqcontrolclosemobilesocket.user_uId_req_control_closemobilesocket(),"0")

    def tearDown(self):
        self.user_uId_req_control_closemobilesocket= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_closemobilesocketTestCase("test_user_uId_req_control_closemobilesocket"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)