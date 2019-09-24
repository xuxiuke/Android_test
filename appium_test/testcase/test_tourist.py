# coding=utf-8

"""
Created on 2018年9月4日

@author: Duke    游客模式测试    15条用例
"""

from appium_test.PO.open_app import Open_app
from appium_test.step import a02_tourist
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test002(unittest.TestCase, a02_tourist.Tourist):  # TestCase类，所有测试用例类继承的基本类
    """游客模式测试"""

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

    # 1、以游客模式登录首页
    def test_home_page(self):
        self.assertTrue(self.home_page())

    # 2、以游客模式点击消息中心
    def test_base_img_right(self):
        self.assertTrue(self.base_img_right(), '未进入登陆页面')

    # 3、以游客模式点击场景
    def test_click_the_scene(self):
        self.assertTrue(self.click_the_scene(), '未进入登陆页面')

    # 4、以游客模式点击【设备】
    def test_click_the_device(self):
        self.assertTrue(self.click_the_device(), '未进入登陆页面')

    # 5、以游客模式点击【发现】
    def test_click_the_find(self):
        self.assertTrue(self.click_the_find(), '未进入发现页面')

    # 6、以游客模式点击【我的】
    def test_click_the_mine(self):
        self.assertTrue(self.click_the_mine(), '未进入我的页面')

    # 7、以游客模式点击【登录/注册】
    def test_click_the_land(self):
        self.assertTrue(self.click_the_land(), '未进入登陆页面')

    # 8、以游客模式点击【网关中心】
    def test_click_the_gateway_center(self):
        self.assertTrue(self.click_the_gateway_center(), '未进入登陆页面')

    # 9、以游客模式点击【分享管理】
    def test_click_the_customer_service(self):
        self.assertTrue(self.click_the_share(), '未进入登陆页面')

    # 10、以游客模式点击【物联会员】
    def test_click_the_member_center(self):
        self.assertTrue(self.click_the_member_center(), '未进入登陆页面')

    # 11、以游客模式点击【意见反馈】
    def test_click_the_customer_feedback(self):
        self.assertTrue(self.click_the_customer_feedback())

    # 12、以游客模式点击【设置】
    def test_click_the_setting(self):
        self.assertTrue(self.click_the_setting(), '未进入登陆页面')

    # 13、以游客模式点击【关于】
    def test_click_the_about(self):
        self.assertTrue(self.click_the_about())

    # 14、以游客模式点击关于页面【功能介绍】
    def test_click_the_about_us_introduction(self):
        self.assertTrue(self.click_the_about_us_introduction())

    # 15、以游客模式点击关于页面【关于物联】
    def test_click_the_about_us_about(self):
        self.assertTrue(self.click_the_about_us_about())
