#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_rememberCurrentDevice_verfyPassword(object):
    def __init__(self):
        pass

    def users_uId_rememberCurrentDevice_verfyPassword(self):
        read_csv = Kernal_function('users/uId/rememberCurrentDevice/verfyPassword')
        return read_csv.iot_put_answer()["resultCode"]

    def dispose(self):
        pass