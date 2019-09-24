#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_third_bind_phonecode import User_third_bind_phonecode
import unittest


class User_third_bind_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userthirdbindphonecode = User_third_bind_phonecode()

    def test_user_third_bind_phonecode(self):
        u""""三方账号绑定账号发送手机验证码"""
        self.assertEqual(self.userthirdbindphonecode.user_third_bind_phonecode(),"0")

    def tearDown(self):
        self.userthirdbindphonecode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_third_bind_phonecodeTestCase("test_user_third_bind_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)