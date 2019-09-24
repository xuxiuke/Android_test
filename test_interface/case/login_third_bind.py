#coding=utf-8

"""
作者: Duke
文件名: login_third_bind.py
创建时间: 2019/09/12-15:48
"""
from  public.main_function import main_function


class Login_third_bind(object):

    @staticmethod
    def login_third_bind():
        read_csv = main_function('login/third/bind')
        return read_csv.sso_post_answer()["resultCode"]
