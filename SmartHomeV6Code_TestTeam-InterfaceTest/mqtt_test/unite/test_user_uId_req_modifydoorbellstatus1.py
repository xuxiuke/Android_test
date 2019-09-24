#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifydoorbellstatus1 import User_uId_req_modifydoorbellstatus1
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifydoorbellstatus1TestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifydoorbellstatus1 = User_uId_req_modifydoorbellstatus1()

    def test_user_uId_req_modifydoorbellstatus1(self):
        u""""mqtt修改门铃为布防状态"""
        self.assertEqual(self.useruIdreqmodifydoorbellstatus1.user_uId_req_modifydoorbellstatus1(),"0")

    def tearDown(self):
        self.user_uId_req_modifydoorbellstatus1= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifydoorbellstatus1TestCase("test_user_uId_req_modifydoorbellstatus1"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)