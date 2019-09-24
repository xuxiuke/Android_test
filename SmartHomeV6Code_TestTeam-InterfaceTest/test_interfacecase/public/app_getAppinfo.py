# coding=utf-8


from test_interfacecase.bussiness.kernal_function import Kernal_function


class App_getAppInfo(object):

    @staticmethod
    def app_getAppInfo():
        read_csv = Kernal_function('app/getAppInfo')
        return read_csv.api_get_answer()["resultCode"]
