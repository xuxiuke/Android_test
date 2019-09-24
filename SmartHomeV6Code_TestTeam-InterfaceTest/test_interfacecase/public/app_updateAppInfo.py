# coding=utf-8

from test_interfacecase.bussiness.kernal_function import Kernal_function


class App_updateAppInfo(object):

    @staticmethod
    def app_updateAppInfo():
        read_csv = Kernal_function('app/updateAppInfo')
        return read_csv.api_post_answer()["resultCode"]
