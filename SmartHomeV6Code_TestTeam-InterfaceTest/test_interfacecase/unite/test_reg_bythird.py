#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.reg_bythird import Reg_bythird
import unittest
import HTMLTestRunner


class Reg_bythirdTestCase(unittest.TestCase):
    def setUp(self):
        self.regbythird = Reg_bythird()


    def test_reg_bythird(self):
        u""""第三方登录,注册信息账户"""
        self.assertEqual(self.regbythird.reg_bythird(),"0")

    def tearDown(self):
        self.regbythird= None




if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Reg_bythirdTestCase("test_reg_bythird"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)