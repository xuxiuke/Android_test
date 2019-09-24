#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Reg_byemailcode(object):
    def __init__(self):
        pass

    def reg_byemailcode(self):
        read_csv = Kernal_function('reg/byemailcode')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass

# reg = Reg_byemailcode()
# reg.reg_byemailcode()