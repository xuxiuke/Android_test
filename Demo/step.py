#coding=utf-8

"""
作者: Duke
文件名: step.py
创建时间: 2020/04/08-08:57
"""

from Demo import base
import time


class Login(base.Action):

    # 1、账号已有住宅情况，登录成功
    def login_success(self):
        self.sign_in_page()  # 登陆页面
        self.login('18013986382', 'wl123456789')
        return self.find_item('我的')  # 验证是否有首页导航栏