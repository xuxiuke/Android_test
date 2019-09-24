#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_remove_user import User_remove_user
import unittest
import HTMLTestRunner


class User_remove_userTestCase(unittest.TestCase):
    def setUp(self):
        self.userremoveuser = User_remove_user()


    def test_user_remove_user(self):
        u""""删除账户信息"""
        self.assertEqual(self.userremoveuser.user_remove_user(),"0")

    def tearDown(self):
        self.userremoveuser= None




if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_remove_userTestCase("test_user_remove_user"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)