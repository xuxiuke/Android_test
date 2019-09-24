#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_devices_grant_deviceId(object):
    def __init__(self):
        pass

    def users_uId_devices_grant_deviceId(self):
        read_csv = Kernal_function('users/uId/devices-grant/deviceId')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):
        pass