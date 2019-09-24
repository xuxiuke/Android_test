#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.login_third_update import Login_third_update
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest
import HTMLTestRunner

class Login_third_updateTestCase(unittest.TestCase):
    def setUp(self):
        self.loginthirdupdate = Login_third_update()


    def test_login_third_update(self):
        u""""三方账号登录绑定手机,替换三方账号"""
        self.assertEqual(self.loginthirdupdate.login_third_update(),"0")

    def tearDown(self):
        read_csv = Kernal_function('login/third/update_recover')
        read_csv.sso_post_answer()["resultCode"]
        self.loginbythird = None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Login_third_updateTestCase("test_login_third_update"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)