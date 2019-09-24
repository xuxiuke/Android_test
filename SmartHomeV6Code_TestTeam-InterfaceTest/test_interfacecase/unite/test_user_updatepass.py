#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_updatepass import User_updatepass
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest
from  test_interfacecase.bussiness.change_phonepassword import Change_phone_password


class User_updatepassTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatepass = User_updatepass()

    def test_user_updatepass(self):
        u""""通过原密码修改密码"""
        self.assertEqual(self.userupdatepass.user_updatepass(),"0")

    def tearDown(self):
        change_phonepassword = Change_phone_password()
        change_phonepassword.change_phone_password()
        self.userupdatepass = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_updatepassTestCase("test_user_updatepass"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)