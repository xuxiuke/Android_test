#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
from  test_interfacecase.public.widget_getUserWidgetInfo_non import Widget_getUserWidgetInfo_non
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout

class Widget_getUserWidgetInfo_nonTestCase(unittest.TestCase):
    def setUp(self):
        self.widgetgetUserWidgetInfonon = Widget_getUserWidgetInfo_non()
        self.loginlogout = Login_logout()


    def test_widget_getUserWidgetInfo_non(self):
        u""""api接口-查询widget信息--未绑定网关"""
        self.assertEqual(self.widgetgetUserWidgetInfonon.widget_getUserWidgetInfo_non(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.widgetgetUserWidgetInfonon= None


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Widget_getUserWidgetInfo_nonTestCase("test_widget_getUserWidgetInfo_non"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)