#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_bythird import Login_bythird
import unittest
import HTMLTestRunner



class Login_bythirdTestCase(unittest.TestCase):
    def setUp(self):
        self.loginbythird = Login_bythird()


    def test_login_bythird(self):
        u""""第三方登录"""
        self.assertEqual(self.loginbythird.login_bythird(),"0")

    def tearDown(self):
        self.loginbythird= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Login_bythirdTestCase("test_login_bythird"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)