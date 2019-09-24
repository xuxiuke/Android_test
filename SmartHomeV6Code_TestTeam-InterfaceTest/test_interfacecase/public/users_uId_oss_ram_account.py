#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_oss_ram_account(object):
    def __init__(self):
        pass

    def users_uId_oss_ram_account(self):
        read_csv = Kernal_function('users/uId/oss/ram/account')
        return read_csv.iot_icamget_answer()["resultCode"]

    def dispose(self):
        pass