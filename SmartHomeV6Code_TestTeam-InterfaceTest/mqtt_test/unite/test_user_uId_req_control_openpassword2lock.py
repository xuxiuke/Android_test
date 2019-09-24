#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_control_openpassword2lock import User_uId_req_control_openpassword2lock
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_control_openpassword2lockTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqcontrolopenpassword2lock = User_uId_req_control_openpassword2lock()

    def test_user_uId_req_control_openpassword2lock(self):
        u""""mqtt打开密码门2锁"""
        self.assertEqual(self.useruIdreqcontrolopenpassword2lock.user_uId_req_control_openpassword2lock(),"0")

    def tearDown(self):
        self.user_uId_req_control_openpassword2lock= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_control_openpassword2lockTestCase("test_user_uId_req_control_openpassword2lock"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)