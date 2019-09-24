#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from test_interfacecase.public.login_byphone import Login_byphone



class Login_byphoneTestCase(unittest.TestCase):
    def setUp(self):
        self.loginbyphone = Login_byphone()

    def test_login_byphone(self):
        u""""密码登录账号"""
        self.assertEqual(self.loginbyphone.login_byphone(),"0")

    def tearDown(self):
        self.loginbyphone= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Login_byphoneTestCase("test_login_byphone"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)






