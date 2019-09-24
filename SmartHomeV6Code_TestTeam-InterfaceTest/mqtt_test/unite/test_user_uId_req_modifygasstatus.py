#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifygasstatus import User_uId_req_modifygasstatus
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifygasstatusTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifygasstatus = User_uId_req_modifygasstatus()

    def test_user_uId_req_modifygasstatus(self):
        u""""mqtt修改可燃气为布防状态"""
        self.assertEqual(self.useruIdreqmodifygasstatus.user_uId_req_modifygasstatus(),"0")

    def tearDown(self):
        self.user_uId_req_modifygasstatus= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifygasstatusTestCase("test_user_uId_req_modifygasstatus"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)