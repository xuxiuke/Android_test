#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Records_uId_devices_deviceId_statistics_humiture(object):
    def __init__(self):
        pass

    def records_uId_devices_deviceId_statistics_humiture(self):
        read_csv = Kernal_function('records/uId/devices/deviceId/statistics_humiture')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):
        pass