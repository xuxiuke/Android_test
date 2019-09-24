#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class User_member_sign(object):
    def __init__(self):
        pass

    def user_member_sign(self):
        read_csv = Kernal_function('user/member/sign')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass