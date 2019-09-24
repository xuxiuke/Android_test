#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class User_third_unbind(object):
    def __init__(self):
        pass

    def user_third_unbind(self):
        read_csv = Kernal_function('user/third/unbind')
        return read_csv.api_post_answer()["resultCode"]

    def dispose(self):
        pass