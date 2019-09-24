#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_update_phone_oldphonecode import User_update_phone_oldphonecode
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_update_phone_oldphonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatephoneoldphonecode = User_update_phone_oldphonecode()
        self.loginlogout = Login_logout()

    def test_user_update_phone_oldphonecode(self):
        u""""修改绑定手机发送手机验证码到旧手机"""
        self.assertEqual(self.userupdatephoneoldphonecode.user_update_phone_oldphonecode(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdatephoneoldphonecode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_update_phone_oldphonecodeTestCase("test_user_update_phone_oldphonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)