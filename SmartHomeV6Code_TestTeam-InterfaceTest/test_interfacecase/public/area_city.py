# coding=utf-8

from test_interfacecase.bussiness.kernal_function import Kernal_function

class Area_city(object):

    @staticmethod
    def area_city():
        read_csv = Kernal_function('area/city')
        return read_csv.api_get_answer()["resultCode"]
