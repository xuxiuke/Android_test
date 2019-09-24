#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_equipmentname import User_uId_req_equipmentname
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_equipmentnameTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqequipmentname = User_uId_req_equipmentname()



    def test_user_uId_req_equipmentname(self):
        u""""mqtt修改温湿度传感器名称"""
        self.assertEqual(self.useruIdreqequipmentname.user_uId_req_equipmentname(),"0")

    def tearDown(self):
        self.useruIdreqequipmentname= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_equipmentnameTestCase("test_user_uId_req_equipmentname"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)