#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class User_update_phone_phonecode(object):
    def __init__(self):
        pass

    def user_update_phone_phonecode(self):
        read_csv = Kernal_function('user/update/phone/phonecode')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass