#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_area_modify import User_uId_req_area_modify
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.public.user_uId_req_arealist import User_uId_req_arealist



class User_uId_req_area_modifyTestCase(unittest.TestCase):
    def setUp(self):
        arealist = User_uId_req_arealist()
        arealist.user_uId_req_arealist()
        self.useruIdreqareamodify = User_uId_req_area_modify()

    def test_user_uId_req_area_modify(self):
        u""""mqtt修改成理查基娜test123区域"""
        self.assertEqual(self.useruIdreqareamodify.user_uId_req_area_modify(),"0")

    def tearDown(self):
        self.user_uId_req_area_modify= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_area_modifyTestCase("test_user_uId_req_area_modify"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)