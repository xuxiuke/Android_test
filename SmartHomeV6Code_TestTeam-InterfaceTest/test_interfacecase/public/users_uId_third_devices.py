#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_third_devices(object):
    def __init__(self):
        pass

    def users_uId_third_devices(self):
        read_csv = Kernal_function('users/uId/third-devices')
        return read_csv.iot_icampost_answer()["resultCode"]

    def dispose(self):
        pass

# user = Users_uId_third_devices()
# user.users_uId_third_devices()