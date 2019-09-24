#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifydoorbellvolume import User_uId_req_modifydoorbellvolume
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifydoorbellvolumeTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifydoorbellvolume = User_uId_req_modifydoorbellvolume()

    def test_user_uId_req_modifydoorbellvolume(self):
        u""""mqtt调整门铃声光器音量"""
        self.assertEqual(self.useruIdreqmodifydoorbellvolume.user_uId_req_modifydoorbellvolume(),"0")

    def tearDown(self):
        self.user_uId_req_modifydoorbellvolume= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifydoorbellvolumeTestCase("test_user_uId_req_modifydoorbellvolume"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)