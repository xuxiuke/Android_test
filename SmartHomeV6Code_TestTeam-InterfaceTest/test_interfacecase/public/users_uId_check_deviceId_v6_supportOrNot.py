#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_check_deviceId_v6_supportOrNot(object):
    def __init__(self):
        pass

    def users_uId_check_deviceId_v6_supportOrNot(self):
        read_csv = Kernal_function('users/uId/check/deviceId/v6/supportOrNot')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):
        pass



#new = Users_uId_check_deviceId_v6_supportOrNot()
#new.users_uId_check_deviceId_v6_supportOrNot()