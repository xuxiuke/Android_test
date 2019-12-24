#coding=utf-8

"""
作者: Duke
文件名: AI01_login.py
创建时间: 2019/12/24-14:26
"""

from appium_test.PO import base_page
from PO import excel
import time


class Login(base_page.Action):

    # 1、登录成功
    def login_success(self):
        if not self.find_item('注册'):
            time.sleep(2)
            self.find_text('我的').click()  # 点击我的
            self.find_text('设置').click()  # 点击设置
            self.find_text('退出登录').click()  # 点击退出登录
            time.sleep(1)
        self.find_text('登录').click()  # 欢迎使用页面点击登录按钮，进入登陆页面
        self.find_text('手机号/邮箱').send_keys('18013986382')
        self.find_text('密码').send_keys('wl123456789')
        self.find_xpath('//android.view.ViewGroup/android.view.ViewGroup[4]').click()  # 点击登陆按钮
        time.sleep(2)
        return self.find_item('我的')  # 验证是否有首页导航栏

    # 2、账号为空
    def none_user(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('username')).send_keys('')
        self.find_id(excel.id_con('password')).send_keys('wl123456789')
        return self.find_id(excel.id_con('login')).is_enabled()  # 验证登录按钮是否可以点击

    # 3、密码为空
    def none_password(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('username')).send_keys('18013986382')
        self.find_id(excel.id_con('password')).send_keys('')
        return self.find_id(excel.id_con('login')).is_enabled()  # 验证登录按钮是否可以点击

    # 4、错误的账号
    def wrong_user(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.login_accountnumber_password('180139863', 'wl123456789')  # 错误账号
        return self.find_toast('账号或密码不正确')

    # 5、错误的密码
    def wrong_password(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.login_accountnumber_password('18013986382', 'wl12345')  # 错误密码
        return self.find_toast('用户密码错误')

    # 6、连续3次密码错误，取消弹窗
    def wrong_password_3(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('username')).send_keys('xxkmtyx@126.com')
        self.find_id(excel.id_con('password')).send_keys('123456')
        for i in range(10):
            self.driver.find_element_by_id(excel.id_con('login')).click()
            time.sleep(1)
            if self.find_item('找回密码'):
                break
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        return self.find_item('找回密码')  # 弹窗已经取消，如果找到返回错误，找不到返回正确

    # 7、连续3次密码错误，找回密码
    def wrong_password_3_findp(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('username')).send_keys('17751027576')
        self.find_id(excel.id_con('password')).send_keys('123456')
        for i in range(10):
            self.find_id(excel.id_con('login')).click()
            time.sleep(1)
            if self.find_item('找回密码'):
                break
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击找回密码按钮
        return self.wait_ac(excel.activity_con('forgot_account_activity'))  # 验证是否进入找回密码页面