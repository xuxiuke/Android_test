#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.area_province import Area_province
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Area_provinceTestCase(unittest.TestCase):
    def setUp(self):
        self.areaprovince = Area_province()
        self.loginlogout = Login_logout()

    def test_area_province(self):
        u"""查询地区接口"""
        self.assertEqual(self.areaprovince.area_province(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.areaprovince = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Area_provinceTestCase("test_area_province"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
