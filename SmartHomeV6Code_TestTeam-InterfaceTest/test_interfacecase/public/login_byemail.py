#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_byemail(object):
    def __init__(self):
        pass

    def login_byemail(self):
        read_csv = Kernal_function('login/byemail')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass



