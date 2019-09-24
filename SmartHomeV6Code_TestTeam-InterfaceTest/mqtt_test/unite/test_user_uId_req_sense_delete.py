#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_sense_delete import User_uId_req_sense_delete
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.public.user_uId_req_senselist import User_uId_req_senselist


class User_uId_req_sense_deleteTestCase(unittest.TestCase):
    def setUp(self):
        new = User_uId_req_senselist()
        new.user_uId_req_senselist()
        self.useruIdreqsensedelete = User_uId_req_sense_delete()

    def test_user_uId_req_sense_delete(self):
        u""""mqtt删除test123456场景任务"""
        self.assertEqual(self.useruIdreqsensedelete.user_uId_req_sense_delete(),"0")

    def tearDown(self):
        self.user_uId_req_sense_delete= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_sense_deleteTestCase("test_user_uId_req_sense_delete"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)