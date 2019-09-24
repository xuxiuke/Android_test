#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_playdoorbellmusic import User_uId_req_playdoorbellmusic
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_playdoorbellmusicTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqplaydoorbellmusic = User_uId_req_playdoorbellmusic()

    def test_user_uId_req_playdoorbellmusic(self):
        u""""mqtt播放门铃声光器音乐状态"""
        self.assertEqual(self.useruIdreqplaydoorbellmusic.user_uId_req_playdoorbellmusic(),"0")

    def tearDown(self):
        self.user_uId_req_playdoorbellmusic= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_playdoorbellmusicTestCase("test_user_uId_req_playdoorbellmusic"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)