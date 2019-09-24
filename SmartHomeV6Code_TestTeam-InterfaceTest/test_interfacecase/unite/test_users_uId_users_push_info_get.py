#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.public.users_uId_users_push_info_get import Users_uId_users_push_info_get
import unittest


class Users_uId_users_push_info_getTestCase(unittest.TestCase):
    def setUp(self):
        self.usersuIduserspushinfoget = Users_uId_users_push_info_get()

    def test_users_uId_users_push_info_get(self):
        u""""查询用户推送信息"""
        self.assertEqual(self.usersuIduserspushinfoget.users_uId_users_push_info_get(),"0")

    def tearDown(self):
        self.usersuIduserspushinfoget = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Users_uId_users_push_info_getTestCase("test_users_uId_users_push_info_get"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)