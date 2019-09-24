#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_users_push_info_get(object):
    def __init__(self):
        pass

    def users_uId_users_push_info_get(self):
        read_csv = Kernal_function('users/uId/users-push-info_get')
        return read_csv.iot_get_answer()["resultCode"]

    def dispose(self):
        pass
