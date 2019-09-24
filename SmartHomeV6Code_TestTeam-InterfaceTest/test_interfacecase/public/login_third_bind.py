#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_third_bind(object):
    def __init__(self):
        pass


    def login_third_bind(self):
        read_csv = Kernal_function('login/third/bind')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass