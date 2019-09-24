#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_wechat_update import User_wechat_update
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout



class User_wechat_updateTestCase(unittest.TestCase):
    def setUp(self):
        self.userwechatupdate = User_wechat_update()
        self.loginlogout = Login_logout()


    def test_user_wechat_update(self):
        u"""物联公众号更改绑定的V6账号"""
        self.assertEqual(self.userwechatupdate.user_wechat_update(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userwechatupdate = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_wechat_updateTestCase("test_user_wechat_update"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)