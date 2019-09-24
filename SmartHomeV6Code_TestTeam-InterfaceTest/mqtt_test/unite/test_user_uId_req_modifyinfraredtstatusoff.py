#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from mqtt_test.public.user_uId_req_modifyinfraredtstatusoff import User_uId_req_modifyinfraredtstatusoff
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifyinfraredtstatusoffTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifyinfraredtstatusoff = User_uId_req_modifyinfraredtstatusoff()

    def test_user_uId_req_modifyinfraredtstatusoff(self):
        u""""mqtt修改红外入侵为撤防状态"""
        self.assertEqual(self.useruIdreqmodifyinfraredtstatusoff.user_uId_req_modifyinfraredtstatusoff(),"0")

    def tearDown(self):
        self.user_uId_req_modifyinfraredtstatusoff= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifyinfraredtstatusoffTestCase("test_user_uId_req_modifyinfraredtstatusoff"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)