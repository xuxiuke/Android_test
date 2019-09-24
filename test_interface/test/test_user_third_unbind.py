# coding=utf-8

"""
作者: Duke
文件名: test_user_third_unbind.py
创建时间: 2019/09/16-11:30
"""

from case.user_third_unbind import User_third_unbind
import unittest
from public import global_value
from case.login_logout import Login_logout


class User_third_unbindTestCase(unittest.TestCase):

    def setUp(self):
        self.userthirdunbind = User_third_unbind()
        self.loginlogout = Login_logout()

    def test_user_third_unbind(self):
        """"在用户中心页面解绑三方账号"""
        self.assertEqual(self.userthirdunbind.user_third_unbind(), "0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userthirdunbind = None
