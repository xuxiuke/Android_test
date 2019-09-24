#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.reg_byemailcode import Reg_byemailcode
import unittest

class Reg_byemailcodeTestCase(unittest.TestCase):
    def setUp(self):
        self.regbyemailcode = Reg_byemailcode()

    def test_reg_byemailcode(self):
        u""""邮箱注册发送邮件"""
        self.assertEqual(self.regbyemailcode.reg_byemailcode(),"0")

    def tearDown(self):
        self.regbyemailcode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Reg_byemailcodeTestCase("test_reg_byemailcode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
