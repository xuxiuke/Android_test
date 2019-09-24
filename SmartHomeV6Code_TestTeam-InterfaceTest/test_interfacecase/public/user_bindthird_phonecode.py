#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class User_bindthird_phonecode(object):
    def __init__(self):
        pass


    def user_bindthird_phonecode(self):
        read_csv = Kernal_function('user/bindthird/phonecode')
        return read_csv.sso_get_answer()["resultCode"]

    def dispose(self):
        pass