#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Feedback_saveFeedback(object):
    def __init__(self):
        pass

    def feedback_saveFeedback(self):
        read_csv = Kernal_function('/feedback/saveFeedback')
        return read_csv.api_post_answer()["resultCode"]

    def dispose(self):
        pass
