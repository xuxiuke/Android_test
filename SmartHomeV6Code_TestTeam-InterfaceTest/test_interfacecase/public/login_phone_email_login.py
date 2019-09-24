#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_phone_email_login(object):
    def __init__(self):
        pass


    def login_phone_email_login(self):
        read_csv = Kernal_function('login/phone/email/login')
        return read_csv.sso_get_answer()["resultCode"]

    def dispose(self):
        pass