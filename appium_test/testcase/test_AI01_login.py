#coding=utf-8

"""
作者: Duke
文件名: test_AI01_login.py
创建时间: 2019/12/24-14:41
"""
from PO.open_app import Open_app
from step import AI01_login
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test001(unittest.TestCase, AI01_login.Login):  # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、账号已有住宅情况，登录成功
    def test_login_success(self):
        self.assertTrue(self.login_success())

    # 2、账号没有住宅情况，登陆成功
    def test_login_success_no_house(self):
        self.assertTrue(self.login_success_no_house())

    # 3、注册页面
    def test_register(self):
        self.assertTrue(self.register())

    # 4、使用条款与免责协议页面
    def test_agreement_page(self):
        self.assertTrue(self.agreement_page())

    # 5、注册页面，获取验证码按钮置灰不可点击
    def test_register_no_phone(self):
        self.assertTrue(self.register_no_phone())

    # 6、注册页面，输入手机号少一位，获取验证码按钮置灰不可点击
    def test_register_phone_10(self):
        self.assertTrue(self.register_phone_10())
