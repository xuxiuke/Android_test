# coding=utf-8

"""
作者: Duke
文件名: AI01_login.py
创建时间: 2019/12/24-14:26
"""

from appium_test.PO import base_page
from PO import excel
import time


class Login(base_page.Action):

    # 前置条件：登录页面，账号登陆
    def login(self, account, password):
        self.find_text('手机号/邮箱').send_keys(account)
        self.find_text('密码').send_keys(password)
        self.find_xpath(excel.xpath_con('login')).click()  # 点击登陆按钮
        time.sleep(2)

    # 前置条件：首页，退出登陆
    def logout(self):
        self.find_text('我的').click()  # 点击我的
        self.find_text('设置').click()  # 点击设置
        self.find_text('退出登录').click()  # 点击退出登录
        time.sleep(1)

    # 1、账号已有住宅情况，登录成功
    def login_success(self):
        if self.find_item('欢迎使用'):  # 未登录情况
            self.find_text('登录').click()  # 点击登录按钮，进入登录页面
        elif self.find_item('添加网关'):  # 账号已登录，没有住宅情况
            self.driver.back()  # 点击返回按钮
            self.logout()  # 退出登录
        else:  # 账号登陆，有住宅情况
            self.logout()  # 退出登录
        self.login('18013986382', 'wl123456789')
        return self.find_item('我的')  # 验证是否有首页导航栏

    # 2、账号没有住宅情况，登陆成功
    def login_success_no_house(self):
        if self.find_item('欢迎使用'):  # 未登录情况
            self.find_text('登录').click()  # 点击登录按钮，进入登录页面
        elif self.find_item('添加网关'):  # 账号已登录，没有住宅情况
            self.driver.back()  # 点击返回按钮
            self.logout()  # 退出登录
        else:  # 账号登陆，有住宅情况
            self.logout()  # 退出登录
        self.login('wlink2019003@126.com', 'v7654321')
        return self.find_item('添加网关')  # 验证是否进入添加网关页面

    # 2、注册页面
