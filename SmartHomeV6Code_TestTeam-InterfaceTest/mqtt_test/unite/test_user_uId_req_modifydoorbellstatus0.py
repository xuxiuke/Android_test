#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_modifydoorbellstatus0 import User_uId_req_modifydoorbellstatus0
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifydoorbellstatus0TestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifydoorbellstatus0 = User_uId_req_modifydoorbellstatus0()

    def test_user_uId_req_modifydoorbellstatus0(self):
        u""""mqtt修改门铃为撤防状态"""
        self.assertEqual(self.useruIdreqmodifydoorbellstatus0.user_uId_req_modifydoorbellstatus0(),"0")

    def tearDown(self):
        self.user_uId_req_modifydoorbellstatus0= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifydoorbellstatus0TestCase("test_user_uId_req_modifydoorbellstatus0"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)