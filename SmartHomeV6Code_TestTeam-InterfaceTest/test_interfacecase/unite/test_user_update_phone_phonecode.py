#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_update_phone_phonecode import User_update_phone_phonecode
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_update_phone_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatephonephonecode = User_update_phone_phonecode()
        self.loginlogout = Login_logout()

    def test_user_update_phone_phonecode(self):
        u""""修改密码发送手机验证码"""
        self.assertEqual(self.userupdatephonephonecode.user_update_phone_phonecode(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdatephonephonecode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_update_phone_phonecodeTestCase("test_user_update_phone_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)