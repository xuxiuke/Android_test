#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.user_phone_update import User_phone_update
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import unittest
import HTMLTestRunner
from  test_interfacecase.bussiness.change_phonenumber import Change_phone_number



class User_phone_updateTestCase(unittest.TestCase):
    def setUp(self):
        self.userphoneupdate = User_phone_update()


    def test_user_phone_update(self):
        u""""API接口-变更手机号"""
        self.assertEqual(self.userphoneupdate.user_phone_update(),"0")


    def tearDown(self):
        changephonenumber = Change_phone_number()
        changephonenumber.change_phone_number()
        self.userphoneupdate = None

     #   self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(User_phone_updateTestCase("test_user_phone_update"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)