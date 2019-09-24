#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_updatepass_phonecode import User_updatepass_phonecode
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class User_updatepass_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userupdatepassphonecode = User_updatepass_phonecode()
        self.loginlogout = Login_logout()

    def test_user_updatepass_phonecode(self):
        u"""修改密码发送手机验证码"""
        self.assertEqual(self.userupdatepassphonecode.user_updatepass_phonecode(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userupdatepassphonecode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_updatepass_phonecodeTestCase("test_user_updatepass_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)