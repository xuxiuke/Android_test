# coding=utf-8

"""
作者: Duke
文件名: test_login_third_update.py
创建时间: 2019/09/16-09:24
"""

from case.login_third_update import Login_third_update
from public.main_function import main_function
import unittest


class Login_third_updateTestCase(unittest.TestCase):

    def setUp(self):
        self.loginthirdupdate = Login_third_update()

    def test_login_third_update(self):
        """"三方账号登录绑定手机,替换三方账号"""
        self.assertEqual(self.loginthirdupdate.login_third_update(), "0")

    def tearDown(self):
        read_csv = main_function('login/third/update_recover')
        read_csv.sso_post_answer()
        self.loginbythird = None
