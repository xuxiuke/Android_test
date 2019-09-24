#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.user_wechat_update_recover import User_wechat_update_recover
from  test_interfacecase.public.login_logout_unbind import Login_logout_unbind
from  test_interfacecase.bussiness import global_value


class User_wechat_update_recoverTestCase(unittest.TestCase):
    def setUp(self):
        self.userwechatupdaterecover = User_wechat_update_recover()
        self.loginlogoutunbind = Login_logout_unbind()

    def test_user_wechat_update_recover(self):
        u""""在用户中心页面解绑微信账号"""
        self.assertEqual(self.userwechatupdaterecover.user_wechat_update_recover(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogoutunbind.login_logout_unbind()
        self.userwechatupdaterecover = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_wechat_update_recoverTestCase("test_user_wechat_update_recover"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)