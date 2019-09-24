#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from test_interfacecase.bussiness.kernal_function import Kernal_function

class Das_weather_current(object):
    def __init__(self):
        pass


    def das_weather_current(self):
        read_csv = Kernal_function('das/weather/current')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass