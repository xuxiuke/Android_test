#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Area_province(object):
    def __init__(self):
        pass


    def area_province(self):
        read_csv = Kernal_function('area/province')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass
