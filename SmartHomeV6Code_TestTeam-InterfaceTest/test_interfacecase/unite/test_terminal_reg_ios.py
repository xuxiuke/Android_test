#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.terminal_reg_ios import Terminal_reg_ios
import unittest
import HTMLTestRunner



class Terminal_reg_iosTestCase(unittest.TestCase):
    def setUp(self):
        self.terminalreg_ios = Terminal_reg_ios()


    def test_terminal_reg_ios(self):
        u""""注册设备ios"""
        self.assertEqual(self.terminalreg_ios.terminal_reg_ios() , "0")

    def tearDown(self):
        self.terminalreg_ios= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Terminal_reg_iosTestCase("test_terminal_reg_ios"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)