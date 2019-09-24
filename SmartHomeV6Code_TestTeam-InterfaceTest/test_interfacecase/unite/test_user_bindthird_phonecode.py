#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.user_bindthird_phonecode import User_bindthird_phonecode

class User_bindthird_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userbindthirdphonecode = User_bindthird_phonecode()


    def test_user_bindthird_phonecode(self):
        u""""三方账号登录时绑定手机号发送验证码"""
        self.assertEqual(self.userbindthirdphonecode.user_bindthird_phonecode(),"0")

    def tearDown(self):
        self.userbindthirdphonecode= None




if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_bindthird_phonecodeTestCase("test_user_bindthird_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)