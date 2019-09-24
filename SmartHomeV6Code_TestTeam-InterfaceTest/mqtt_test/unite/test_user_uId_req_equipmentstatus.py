#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_equipmentstatus import User_uId_req_equipmentstatus
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_equipmentstatusTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqequipmentstatus = User_uId_req_equipmentstatus()



    def test_user_uId_req_equipmentstatus(self):
        u""""mqtt修改门窗磁撤防状态"""
        self.assertEqual(self.useruIdreqequipmentstatus.user_uId_req_equipmentstatus(),"0")

    def tearDown(self):
        self.useruIdreqequipmentstatus= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_equipmentstatusTestCase("test_user_uId_req_equipmentstatus"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)