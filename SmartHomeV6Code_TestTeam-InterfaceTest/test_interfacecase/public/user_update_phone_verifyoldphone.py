#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class User_update_phone_verifyoldphone(object):
    def __init__(self):
        pass

    def user_update_phone_verifyoldphone(self):
        read_csv = Kernal_function('user/update/phone/verifyoldphone')
        return read_csv.api_post_answer()["resultCode"]

    def dispose(self):
        pass