#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_third_update(object):
    def __init__(self):
        pass


    def login_third_update(self):
        read_csv = Kernal_function('login/third/update')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass

