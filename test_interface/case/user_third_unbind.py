#coding=utf-8

"""
作者: Duke
文件名: user_third_unbind.py
创建时间: 2019/09/16-11:32
"""

from  public.main_function import main_function


class User_third_unbind(object):

    @staticmethod
    def user_third_unbind():
        read_csv = main_function('user/third/unbind')
        return read_csv.api_post_answer()["resultCode"]