#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_delete_sixsenseswitch import  User_uId_req_delete_sixsenseswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_delete_sixsenseswitchTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqdeletesixsenseswitch = User_uId_req_delete_sixsenseswitch()

    def test_user_uId_req_delete_sixsenseswitch(self):
        u""""mqtt6键场景开关删除场景"""
        self.assertEqual(self.useruIdreqdeletesixsenseswitch.user_uId_req_delete_sixsenseswitch(),"0")

    def tearDown(self):
        self.user_uId_req_delete_sixsenseswitch= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_delete_sixsenseswitchTestCase("test_user_uId_req_delete_sixsenseswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)