#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Theme_getAllTheme(object):
    def __init__(self):
        pass


    def theme_getAllTheme(self):
        read_csv = Kernal_function('theme/getAllTheme')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass
