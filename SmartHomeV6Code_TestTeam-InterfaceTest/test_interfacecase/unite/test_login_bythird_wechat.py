#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.login_bythird_wechat import Login_bythird_wechat
import unittest
import HTMLTestRunner



class Login_bythird_wechatTestCase(unittest.TestCase):
    def setUp(self):
        self.loginbythirdwechat = Login_bythird_wechat()


    def test_login_bythird_wechat(self):
        u""""第三方微信登录"""
        self.assertEqual(self.loginbythirdwechat.login_bythird_wechat(),"0")

    def tearDown(self):
        self.loginbythirdwechat= None



if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Login_bythird_wechatTestCase("test_login_bythird_wechat"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)