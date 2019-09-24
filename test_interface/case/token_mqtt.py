#coding=utf-8

"""
作者: Duke
文件名: token_mqtt.py
创建时间: 2019/09/12-15:09
"""

from  public.main_function import main_function

class Token_mqtt(object):

    @staticmethod
    def token_mqtt():
        read_csv = main_function('token/mqtt')
        return read_csv.sso_get_answer()["resultCode"]
