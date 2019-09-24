#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.public.das_weather_current import Das_weather_current
import unittest
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Das_weather_currentTestCase(unittest.TestCase):
    def setUp(self):
        self.dasweathercurrent = Das_weather_current()
        self.loginlogout = Login_logout()

    def test_das_weather_current(self):
        u"""查询城市的天气温湿度接口"""
        self.assertEqual(self.dasweathercurrent.das_weather_current(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.dasweathercurrent = None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Das_weather_currentTestCase("test_das_weather_current"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)