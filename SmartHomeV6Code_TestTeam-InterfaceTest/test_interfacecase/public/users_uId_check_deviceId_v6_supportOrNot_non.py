#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_check_deviceId_v6_supportOrNot_non(object):
    def __init__(self):
        pass

    def users_uId_check_deviceId_v6_supportOrNot_non(self):
        read_csv = Kernal_function('users/uId/check/deviceId/v6/supportOrNot_non')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):

        pass



