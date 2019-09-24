#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_third_unbind import User_third_unbind
import unittest
from  test_interfacecase.bussiness import global_value
from  test_interfacecase.public.login_logout import Login_logout


class User_third_unbindTestCase(unittest.TestCase):
    def setUp(self):
        self.userthirdunbind = User_third_unbind()
        self.loginlogout = Login_logout()

    def test_user_third_unbind(self):
        u""""在用户中心页面解绑三方账号"""
        self.assertEqual(self.userthirdunbind.user_third_unbind(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userthirdunbind = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_third_unbindTestCase("test_user_third_unbind"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
