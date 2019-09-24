#coding=utf-8

"""
作者: Duke
文件名: app_getAppinfo.py
创建时间: 2019/09/11-17:06
"""

from public.main_function import main_function


class App_getAppInfo(object):

    @staticmethod
    def app_getAppInfo():
        read_csv = main_function('app/getAppInfo')
        return read_csv.api_get_answer()["resultCode"]