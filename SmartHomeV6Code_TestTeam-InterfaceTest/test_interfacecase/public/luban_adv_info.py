#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Luban_adv_info(object):
    def __init__(self):
        pass

    def luban_adv_info_CN(self):
        read_csv = Kernal_function('luban/adv/info_CN')
        return read_csv.api_get_answer()["resultCode"]

    def luban_adv_info_en(self):
        read_csv = Kernal_function('luban/adv/info_en')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass



