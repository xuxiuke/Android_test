#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_update_phone_verifyoldphone import User_update_phone_verifyoldphone
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_update_phone_verifyoldphoneTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatephoneverifyoldphone = User_update_phone_verifyoldphone()
        self.loginlogout = Login_logout()

    def test_user_update_phone_verifyoldphone(self):
        u""""变更手机号校验旧手机的验证码"""
        self.assertEqual(self.userupdatephoneverifyoldphone.user_update_phone_verifyoldphone(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdatephoneverifyoldphone = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_update_phone_verifyoldphoneTestCase("test_user_update_phone_verifyoldphone"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)