#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



import unittest
from mqtt_test.public.user_uId_req_modifyinfraredtstatus import User_uId_req_modifyinfraredtstatus
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifyinfraredtstatusTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifyinfraredtstatus = User_uId_req_modifyinfraredtstatus()

    def test_user_uId_req_modifyinfraredtstatus(self):
        u""""mqtt修改红外入侵为布防状态"""
        self.assertEqual(self.useruIdreqmodifyinfraredtstatus.user_uId_req_modifyinfraredtstatus(),"0")

    def tearDown(self):
        self.user_uId_req_modifyinfraredtstatus= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifyinfraredtstatusTestCase("test_user_uId_req_modifyinfraredtstatus"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)