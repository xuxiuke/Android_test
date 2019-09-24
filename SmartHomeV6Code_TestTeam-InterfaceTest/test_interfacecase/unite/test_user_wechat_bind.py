#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_wechat_bind import User_wechat_bind
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout
from  test_interfacecase.public.user_third_unbind import User_third_unbind


class User_wechat_bindTestCase(unittest.TestCase):
    def setUp(self):
        self.userwechatbind = User_wechat_bind()
        self.loginlogout = Login_logout()
        self.userthirdunbind = User_third_unbind()

    def test_user_wechat_bind(self):
        u"""物联公众号绑定V6账号"""
        self.assertEqual(self.userwechatbind.user_wechat_bind(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        # self.userthirdunbind.user_third_unbind()
        # self.loginlogout.login_logout()
        # self.userthirdunbind = None
        self.userwechatbind = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_wechat_bindTestCase("test_user_wechat_bind"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)