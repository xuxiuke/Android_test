#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.login_third_bind import Login_third_bind
import unittest
import HTMLTestRunner

class Login_third_bindTestCase(unittest.TestCase):
    def setUp(self):
        self.loginthirdbind = Login_third_bind()


    def test_login_third_bind(self):
        u""""三方账号登录绑定手机"""
        self.assertEqual(self.loginthirdbind.login_third_bind(),"0")

    def tearDown(self):
        self.loginthirdbind= None




if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Login_third_bindTestCase("test_login_third_bind"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)