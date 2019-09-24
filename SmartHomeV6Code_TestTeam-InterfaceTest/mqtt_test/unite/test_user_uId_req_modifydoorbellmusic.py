#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_modifydoorbellmusic import User_uId_req_modifydoorbellmusic
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifydoorbellmusicTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifydoorbellmusic = User_uId_req_modifydoorbellmusic()

    def test_user_uId_req_modifydoorbellmusic(self):
        u""""mqtt切换门铃声光器音乐"""
        self.assertEqual(self.useruIdreqmodifydoorbellmusic.user_uId_req_modifydoorbellmusic(),"0")

    def tearDown(self):
        self.user_uId_req_modifydoorbellmusic= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifydoorbellmusicTestCase("test_user_uId_req_modifydoorbellmusic"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)