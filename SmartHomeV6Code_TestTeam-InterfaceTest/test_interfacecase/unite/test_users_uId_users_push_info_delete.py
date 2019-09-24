#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.users_uId_users_push_info_delete import Users_uId_users_push_info_delete
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Users_uId_users_push_info_deleteTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIduserspushinfodelete = Users_uId_users_push_info_delete()
        self.loginlogout = Login_logout()

    def test_users_uId_users_push_info_delete(self):
        u""""删除用户推送信息"""
        self.assertEqual(self.usersuIduserspushinfodelete.users_uId_users_push_info_delete(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.usersuIduserspushinfodelete = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_users_push_info_deleteTestCase("test_users_uId_users_push_info_delete"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)