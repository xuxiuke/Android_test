#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.reg_phonecode import Reg_phonecode

class Reg_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.regphonecode = Reg_phonecode()


    def test_reg_phonecode(self):
        u""""手机注册时发送验证码"""
        self.assertEqual(self.regphonecode.reg_phonecode(),"0")

    def tearDown(self):
        self.regphonecode= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Reg_phonecodeTestCase("test_reg_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
