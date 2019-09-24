#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_devices_deleteAlarmInfo_msg(object):
    def __init__(self):
        pass

    def users_uId_devices_deleteAlarmInfo_msg(self):
        read_csv = Kernal_function('users/uId/devices/deleteAlarmInfo_msg')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):
        pass