#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.terminal_reg_android import Terminal_reg_addroid
import unittest
import HTMLTestRunner



class Terminal_reg_addroidTestCase(unittest.TestCase):
    def setUp(self):
        self.terminalreg_android = Terminal_reg_addroid()


    def test_terminal_reg_android(self):
        u""""注册设备安卓"""
        self.assertEqual(self.terminalreg_android.terminal_reg_addroid() , "0")

    def tearDown(self):
        self.terminalreg_android= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Terminal_reg_addroidTestCase("test_terminal_reg_android"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
