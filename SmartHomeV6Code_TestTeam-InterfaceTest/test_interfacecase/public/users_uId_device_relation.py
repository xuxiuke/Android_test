#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Users_uId_device_relation(object):
    def __init__(self):
        pass

    def users_uId_device_relation(self):
        read_csv = Kernal_function('users/uId/device-relation')
        return read_csv.iot_post_answer()["resultCode"]

    def dispose(self):
        pass

# user = Users_uId_device_relation()
# user.users_uId_device_relation()
