#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_sense_modify import User_uId_req_sense_modify
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.public.user_uId_req_senselist import User_uId_req_senselist



class User_uId_req_sense_modifyTestCase(unittest.TestCase):
    def setUp(self):
        new = User_uId_req_senselist()
        new.user_uId_req_senselist()
        self.useruIdreqsensemodify = User_uId_req_sense_modify()
        print("need is", global_value.get_return_sceneID_value())

    def test_user_uId_req_sense_modify(self):
        u""""mqtt修改test123变成test123456场景任务名称"""
        self.assertEqual(self.useruIdreqsensemodify.user_uId_req_sense_modify(),"0")

    def tearDown(self):
        self.user_uId_req_sense_modify= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_sense_modifyTestCase("test_user_uId_req_sense_modify"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)