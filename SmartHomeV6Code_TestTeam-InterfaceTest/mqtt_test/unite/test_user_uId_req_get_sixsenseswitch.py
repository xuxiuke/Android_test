#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_get_sixsenseswitch import User_uId_req_get_sixsenseswitch
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_get_sixsenseswitchTestCase(unittest.TestCase):
    def setUp(self):


        self.useruIdreqgetsixsenseswitch = User_uId_req_get_sixsenseswitch()


    def test_user_uId_req_get_sixsenseswitch(self):
        u""""mqtt查询六键场景开关绑定场景列表"""
        self.assertEqual(self.useruIdreqgetsixsenseswitch.user_uId_req_get_sixsenseswitch(),"0")

    def tearDown(self):
        self.useruIdreqgetsixsenseswitch= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_get_sixsenseswitchTestCase("test_user_uId_req_get_sixsenseswitch"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)