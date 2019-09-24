#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import unittest
import HTMLTestRunner
from  test_interfacecase.public.records_uId_devices_deviceId_statistics_humiture import Records_uId_devices_deviceId_statistics_humiture
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Records_uId_devices_deviceId_statistics_humitureTestCase(unittest.TestCase):
    def setUp(self):
        self.recordsuIddevicesdeviceIdstatisticshumiture = Records_uId_devices_deviceId_statistics_humiture()
        self.loginlogout = Login_logout()


    def test_records_uId_devices_deviceId_statistics_humiture(self):
        u""""可查询humiture统计数据"""
        self.assertEqual(self.recordsuIddevicesdeviceIdstatisticshumiture.records_uId_devices_deviceId_statistics_humiture(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.recordsuIddevicesdeviceIdstatisticshumiture= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Records_uId_devices_deviceId_statistics_humitureTestCase("test_records_uId_devices_deviceId_statistics_humiture"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)