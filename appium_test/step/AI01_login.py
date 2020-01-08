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

    # 3、注册页面
    def register(self):
        if self.find_item('欢迎使用'):  # 未登录情况
            pass
        elif self.find_item('添加网关'):  # 账号已登录，没有住宅情况
            self.driver.back()  # 点击返回按钮
            self.logout()  # 退出登录
            self.driver.back()  # 点击返回按钮
        else:  # 账号登陆，有住宅情况
            self.logout()  # 退出登录
            self.driver.back()  # 点击返回按钮
        self.find_text('注册').click()  # 点击注册按钮
        return self.find_item('注册即代表阅读并同意')

    # 4、使用条款与免责协议页面
    def agreement_page(self):
        self.register()  # 注册页面
        self.find_text('《使用条款与免责协议》').click()  # 点击使用条款与免责协议
        time.sleep(3)
        return self.find_item('《使用条款与免责协议》')

    # 5、注册页面，获取验证码按钮置灰不可点击
    def register_no_phone(self):
        self.register()  # 注册页面
        # self.find_text('手机号/邮箱').send_keys('18013986382')
        self.find_text('获取验证码').click()  # 点击获取验证码
        return self.find_item('获取验证码')  # 验证是否在注册页面

    # 6、注册页面，输入手机号少一位，获取验证码按钮置灰不可点击
    def register_phone_10(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('1801398638')
        return self.get_colour_text('获取验证码')  # 验证按钮颜色是否正确

    # 7、注册页面，输入手机号，获取验证码按钮可以点击
    def register_right_phone(self):
        pass

    # 8、注册页面，输入已注册手机号，点击获取验证码按钮，弹窗手机号已被注册
    def register_phone_used(self):
        pass

    # 9、注册页面手机号已被注册弹窗，点击取消按钮，弹窗消失
    def register_popup_cancel(self):
        pass

    # 10、注册页面手机号已被注册弹窗，点击去登录按钮，进入登录页面
    def register_land(self):
        pass

    # 11、注册页面，输入未注册手机号，点击获取验证码按钮，进入输入验证码页面
    def register_code_page(self):
        pass

    # 12、注册-输入验证码页面，输入错误验证码，提示验证码错误
    def code_page_wrongcode(self):
        pass
