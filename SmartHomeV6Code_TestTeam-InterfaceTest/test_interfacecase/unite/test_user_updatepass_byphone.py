#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.change_phonepassword import Change_phone_password
from  test_interfacecase.public.user_updatepass_byphone import User_updatepass_byphone
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest


class User_updatepass_byphoneTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatepassbyphone = User_updatepass_byphone()

    def test_user_updatepass_byphone(self):
        u""""手机号+验证码修改用户密码"""
        self.assertEqual(self.userupdatepassbyphone.user_updatepass_byphone(),"0")

    def tearDown(self):
        change_phonepassword = Change_phone_password()
        change_phonepassword.change_phone_password()
        self.userupdatepassbyphone = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_updatepass_byphoneTestCase("test_user_updatepass_byphone"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)