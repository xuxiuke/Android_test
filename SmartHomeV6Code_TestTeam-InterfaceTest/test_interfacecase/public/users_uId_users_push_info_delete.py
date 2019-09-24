#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_users_push_info_delete(object):
    def __init__(self):
        pass

    def users_uId_users_push_info_delete(self):
        read_csv = Kernal_function('users/uId/users-push-info_delete')
        return read_csv.iot_delete_answer()["resultCode"]

    def dispose(self):
        pass
