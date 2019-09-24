#coding=utf-8

"""
作者: Duke
文件名: login_bythird.py
创建时间: 2019/09/12-15:24
"""

from  public.main_function import main_function


class Login_bythird(object):

    @staticmethod
    def login_bythird():
        read_csv = main_function('login/bythird')
        return read_csv.sso_post_answer()["resultCode"]
