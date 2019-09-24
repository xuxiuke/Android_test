#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.records_uId_devices_deviceId_statistics_CO2 import Records_uId_devices_deviceId_statistics_CO2
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Records_uId_devices_deviceId_statistics_CO2TestCase(unittest.TestCase):
    def setUp(self):
        self.recordsuIddevicesdeviceIdstatisticsCO2 = Records_uId_devices_deviceId_statistics_CO2()
        self.loginlogout = Login_logout()


    def test_records_uId_devices_deviceId_statistics_CO2(self):
        u""""可查询CO2统计数据"""
        self.assertEqual(self.recordsuIddevicesdeviceIdstatisticsCO2.records_uId_devices_deviceId_statistics_CO2(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.recordsuIddevicesdeviceIdstatisticsCO2= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Records_uId_devices_deviceId_statistics_CO2TestCase("test_records_uId_devices_deviceId_statistics_CO2"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)