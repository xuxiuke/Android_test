#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.theme_getAllTheme import Theme_getAllTheme
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Theme_getAllThemeTestCase(unittest.TestCase):
    def setUp(self):
        self.themegetAllTheme = Theme_getAllTheme()
        self.loginlogout = Login_logout()


    def test_theme_getAllTheme(self):
        u""""获取皮肤主题列表"""
        self.assertEqual(self.themegetAllTheme.theme_getAllTheme(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.themegetAllTheme= None

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Theme_getAllThemeTestCase("test_theme_getAllTheme"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)

