#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifysmokedetectorstatus import User_uId_req_modifysmokedetectorstatus
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifysmokedetectorstatusTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifysmokedetectorstatus = User_uId_req_modifysmokedetectorstatus()

    def test_user_uId_req_modifysmokedetectorstatus(self):
        u""""mqtt修改烟感为撤防状态"""
        self.assertEqual(self.useruIdreqmodifysmokedetectorstatus.user_uId_req_modifysmokedetectorstatus(),"0")

    def tearDown(self):
        self.user_uId_req_modifysmokedetectorstatus= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifysmokedetectorstatusTestCase("test_user_uId_req_modifysmokedetectorstatus"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)