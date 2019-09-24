#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class User_remove_user(object):
    def __init__(self):
        pass

    def user_remove_user(self):
        read_csv = Kernal_function('user/remove/user')
        return read_csv.sso_get_answer()["resultCode"]

    def dispose(self):
        pass