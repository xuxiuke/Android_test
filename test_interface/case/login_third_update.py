# coding=utf-8

"""
作者: Duke
文件名: login_third_update.py
创建时间: 2019/09/16-09:29
"""

from public.main_function import main_function


class Login_third_update(object):

    @staticmethod
    def login_third_update():
        read_csv = main_function('login/third/update')
        return read_csv.sso_post_answer()["resultCode"]
