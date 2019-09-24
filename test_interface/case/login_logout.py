# coding=utf-8

"""
作者: Duke
文件名: login_logout.py
创建时间: 2019/09/11-17:11
"""

from public.main_function import main_function


class Login_logout(object):

    @staticmethod
    def login_logout():
        read_csv = main_function('login/logout')
        return read_csv.sso_post_answer()["resultCode"]
