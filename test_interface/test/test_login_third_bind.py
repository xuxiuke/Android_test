# coding=utf-8

"""
作者: Duke
文件名: test_login_third_bind.py
创建时间: 2019/09/12-15:47
"""
from case.login_third_bind import Login_third_bind
import unittest


class Login_third_bindTestCase(unittest.TestCase):

    def setUp(self):
        self.loginthirdbind = Login_third_bind()

    def test_login_third_bind(self):
        """"三方账号登录绑定手机"""
        self.assertEqual(self.loginthirdbind.login_third_bind(), "0")

    def tearDown(self):
        self.loginthirdbind = None
