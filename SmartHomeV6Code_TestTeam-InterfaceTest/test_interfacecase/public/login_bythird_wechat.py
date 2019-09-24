#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Login_bythird_wechat(object):
    def __init__(self):   #,status_code = 200
        pass

    def login_bythird_wechat(self):
        read_csv = Kernal_function('login/bythird_wechat')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass
