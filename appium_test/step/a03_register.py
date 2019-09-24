# coding=utf-8

"""
Created on 2018年9月5日

@author: Duke    注册+忘记密码，大部分用例无法翻译
"""

from appium_test.PO import base_page
from PO import excel
import time

class Register(base_page.Action):

    # 1、进入注册页
    def click_the_register(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(1)
        return self.find_item('输入手机号码')  # 验证页面是否有text输入手机号码

    # 2、手机号格式不正确
    def incorrect_format(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('123456')  # 输入错误手机号
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        return self.find_toast('手机号格式错误')  # 验证toast是否正确

    # 3、手机号已被注册-用户已存在
    def account_is_registered(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('18013986382')  # 输入错误手机号
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        return self.find_toast('用户已存在')  # 验证toast是否正确

    # 4、手机号码为空下一步按钮不可点击
    def next_step_not_clickable(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(2)
        return self.find_id(excel.id_con('tv_get_verification')).is_enabled()  # 验证按钮是否可以点击

    # 5、《使用条款与免责协议》
    def disclaimer_agreement(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(2)
        self.find_id(excel.id_con('tv_terms_of_use')).click()  # 点击使用条款和免责协议
        time.sleep(5)
        return self.find_item('南京物联传感技术有限公司')  # 验证页面是否有text南京物联传感技术有限公司

    # 6、《使用条款与免责协议》页面返回注册页面
    def return_register(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('register')).click()  # 点击注册按钮
        time.sleep(2)
        self.find_id(excel.id_con('tv_terms_of_use')).click()  # 点击使用条款和免责协议
        time.sleep(2)
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_item('输入手机号码')  # 验证页面是否有text输入手机号码

    # 7、进入忘记密码页面
    def forget_the_password(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(1)
        return self.find_item('输入手机号或邮箱')  # 验证页面是否有text输入手机号或邮箱

    # 8、忘记密码，手机号格式不正确
    def password_incorrect_format(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('123456')  # 输入错误手机号
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        return self.find_toast('请输入正确的邮箱或手机号')  # 验证toast是否正确

    # 9、未输入手机号，下一步按钮不可点击
    def password_not_clickable(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(2)
        return self.find_id(excel.id_con('tv_get_verification')).is_enabled()  # 验证按钮是否可以点击

    # 10、新密码设置成功,返回登陆页面
    def new_password(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('18013986382')
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        time.sleep(3)
        self.input_validation_code()  # 输入验证码1-6
        time.sleep(2)
        self.find_id(excel.id_con('et_pwd')).send_keys('wl123456789')  # 输入新密码
        self.find_id(excel.id_con('tv_sure')).click()  # 点击完成按钮
        # return self.find_toast('新密码设置成功')
        return self.wait_ac(excel.activity_con('signin_activity'))  # 注册页面

    # 11、错误的验证码
    def error_validation_code(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('18013986382')
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        time.sleep(3)
        self.input_error_validation_code()  # 输入错误验证码
        time.sleep(2)
        return self.find_toast('验证码错误')

    # 12、新密码不足6位
    def password_less_6(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_id(excel.id_con('item_account_login_name')).click()
        self.wait_ac(excel.activity_con('signin_activity'))
        self.find_id(excel.id_con('login_error')).click()  # 点击忘记密码按钮
        time.sleep(2)
        self.find_id(excel.id_con('et_account')).send_keys('18013986382')
        self.find_id(excel.id_con('tv_get_verification')).click()  # 点击下一步按钮
        time.sleep(3)
        self.input_validation_code()  # 输入验证码1-6
        time.sleep(2)
        self.find_id(excel.id_con('et_pwd')).send_keys('wl123')  # 输入小于6位新密码
        self.find_id(excel.id_con('tv_sure')).click()  # 点击完成按钮
        return self.find_toast('密码长度不能小于8个字符')
