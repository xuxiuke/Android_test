#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Partner_tokens(object):
    def __init__(self):
        pass

    def partner_tokens(self):
        read_csv = Kernal_function('partner/tokens')
        return read_csv.api_post_answer()["resultCode"]

    def dispose(self):
        pass