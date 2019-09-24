#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_controlequipment import User_uId_req_controlequipment
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_controlequipmentTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolequipment = User_uId_req_controlequipment()



    def test_user_uId_req_controlequipment(self):
        u""""mqtt打开二路开关的一路开关"""
        self.assertEqual(self.useruIdreqcontrolequipment.user_uId_req_controlequipment(),"0")

    def tearDown(self):
        self.useruIdreqcontrolequipment= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_controlequipmentTestCase("test_user_uId_req_controlequipment"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)