#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.widget_getUserWidgetInfo import Widget_getUserWidgetInfo
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Widget_getUserWidgetInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.widgetgetUserWidgetInfo = Widget_getUserWidgetInfo()
        self.loginlogout = Login_logout()


    def test_widget_getUserWidgetInfo(self):
        u""""api接口-查询widget信息--为绑定网关"""
        self.assertEqual(self.widgetgetUserWidgetInfo.widget_getUserWidgetInfo(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.widgetgetUserWidgetInfo= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Widget_getUserWidgetInfoTestCase("test_widget_getUserWidgetInfo"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)
