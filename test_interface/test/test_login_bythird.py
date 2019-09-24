# coding=utf-8

"""
作者: Duke
文件名: test_login_bythird.py
创建时间: 2019/09/12-15:20
"""

from case.login_bythird import Login_bythird
import unittest


class Login_bythirdTestCase(unittest.TestCase):
    def setUp(self):
        self.loginbythird = Login_bythird( )

    def test_login_bythird(self):
        """"第三方登录"""
        self.assertEqual(self.loginbythird.login_bythird(), "0")

    def tearDown(self):
        self.loginbythird = None
