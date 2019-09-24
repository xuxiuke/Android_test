#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Slideshow_getAllSlides(object):
    def __init__(self):
        pass

    def slideshow_getAllSlides(self):
        read_csv = Kernal_function('slideshow/getAllSlides')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass