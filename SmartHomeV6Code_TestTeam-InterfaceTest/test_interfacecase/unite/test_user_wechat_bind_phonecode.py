#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.user_wechat_bind_phonecode import User_wechat_bind_phonecode
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class User_wechat_bind_phonecodeTestCase(unittest.TestCase):
    def setUp(self):
        self.userwechatbindphonecode = User_wechat_bind_phonecode()
        self.loginlogout = Login_logout()

    def test_user_wechat_bind_phonecode(self):
        u"""物联公众号绑定V6账号发送验证码"""
        self.assertEqual(self.userwechatbindphonecode.user_wechat_bind_phonecode(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.userwechatbindphonecode = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_wechat_bind_phonecodeTestCase("test_user_wechat_bind_phonecode"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)