#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Terminal_reg_ios(object):
    def __init__(self):
        pass

    def terminal_reg_ios(self):
        read_csv = Kernal_function('terminal/reg_ios')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass
