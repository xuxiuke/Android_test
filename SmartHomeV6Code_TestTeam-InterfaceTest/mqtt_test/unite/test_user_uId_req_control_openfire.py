#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_control_openfire import User_uId_req_control_openfire
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openfireTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenfire = User_uId_req_control_openfire()

    def test_user_uId_req_control_openfire(self):
        u""""mqtt打开火警开关"""
        self.assertEqual(self.useruIdreqcontrolopenfire.user_uId_req_control_openfire(),"0")

    def tearDown(self):
        self.user_uId_req_control_openfire= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openfireTestCase("test_user_uId_req_control_openfire"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)