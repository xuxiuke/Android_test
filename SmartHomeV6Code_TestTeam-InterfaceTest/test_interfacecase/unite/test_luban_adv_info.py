#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.luban_adv_info import Luban_adv_info
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Luban_adv_infoTestCase(unittest.TestCase):
    def setUp(self):
        self.lubanadvinfo = Luban_adv_info()
        self.loginlogout = Login_logout()


    def test_luban_adv_info_CN(self):
        u""""获取中文语言下广告"""
        self.assertEqual(self.lubanadvinfo.luban_adv_info_CN(),"0")

    def test_luban_adv_info_en(self):
        u""""获取英文语言下广告"""
        self.assertEqual(self.lubanadvinfo.luban_adv_info_en(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.lubanadvinfo = None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Luban_adv_infoTestCase("test_luban_adv_info_CN"))
    suite.addTest(Luban_adv_infoTestCase("test_luban_adv_info_en"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)