#coding=utf-8

"""
Created on 2018年11月01日

@author: Duke    添加多个场景和区域    2条用例
"""

from PO.open_app import Open_app
from step import case
import unittest
import time

@unittest.skip(u'添加场景、区域，跳过测试')
class Test011(unittest.TestCase, case.Case): # TestCase类，所有测试用例类继承的基本类
    """添加多个场景和区域"""
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

    # 添加16个场景，1-16
    # @unittest.skip(u'添加16个场景，跳过测试')
    def test_add_scene(self):
        self.add_scene()

    # 添加ABCDEFGHUJKLMNOP区域
    # @unittest.skip(u'添加16个区域，跳过测试')
    def test_add_zone(self):
        self.add_zone()