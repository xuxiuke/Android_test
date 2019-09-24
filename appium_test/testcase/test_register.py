#coding=utf-8

"""
Created on 2018年9月5日

@author: Duke    注册测试+忘记密码    12条用例
"""

from PO.open_app import Open_app
from step import a03_register
import unittest
import time

# @unittest.skip(u'添加场景、区域，跳过测试')
class Test003(unittest.TestCase, a03_register.Register): # TestCase类，所有测试用例类继承的基本类
    """注册测试+忘记密码"""
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

    # 1、进入注册页
    def test_click_the_regidter(self):
        self.assertTrue(self.click_the_register())

    # 2、手机号格式不正确
    def test_incorrect_format(self):
        self.assertTrue(self.incorrect_format())

    # 3、手机号已被注册-用户已存在
    def test_account_is_registered(self):
        self.assertTrue(self.account_is_registered())

    # 4、手机号码为空下一步按钮不可点击
    def test_next_step_not_clickable(self):
        self.assertFalse(self.next_step_not_clickable())

    # 5、《使用条款与免责协议》
    def test_disclaimer_agreement(self):
        self.assertTrue(self.disclaimer_agreement())

    # 6、《使用条款与免责协议》页面返回注册页面
    def test_return_register(self):
        self.assertTrue(self.return_register())

    # 7、进入忘记密码页面
    def test_forget_the_password(self):
        self.assertTrue(self.forget_the_password())

    # 8、忘记密码，手机号格式不正确
    def test_password_incorrect_format(self):
        self.assertTrue(self.password_incorrect_format())

    # 9、未输入手机号，下一步按钮不可点击
    def test_password_not_clickable(self):
        self.assertFalse(self.password_not_clickable())

    # 10、新密码设置成功
    def test_new_password(self):
        self.assertTrue(self.new_password())

    # 11、输入错误的验证码
    def test_error_validation_code(self):
        self.assertTrue(self.error_validation_code())

    # 12、新密码不足6位
    def test_password_less_6(self):
        self.assertTrue(self.password_less_6())