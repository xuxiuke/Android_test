#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
import HTMLTestRunner
from  test_interfacecase.public.records_uId_devices_deviceId import Records_uId_devices_deviceId
from  test_interfacecase.bussiness import global_value
from test_interfacecase.public.login_logout import Login_logout


class Records_uId_devices_deviceIdTestCase(unittest.TestCase):
    def setUp(self):
        self.recordsuIddevicesdeviceId = Records_uId_devices_deviceId()
        self.loginlogout = Login_logout()


    def test_records_uId_devices_deviceId(self):
        u""""可查询设备告警、用户操作数据"""
        self.assertEqual(self.recordsuIddevicesdeviceId.records_uId_devices_deviceId(),"0")

    def tearDown(self):
        global_value.set_execute_value("1")
        self.loginlogout.login_logout()
        self.recordsuIddevicesdeviceId= None


if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(Records_uId_devices_deviceIdTestCase("test_records_uId_devices_deviceId"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)