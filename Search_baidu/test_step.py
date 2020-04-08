#coding=utf-8

"""
作者: Duke
文件名: test_step.py
创建时间: 2020/04/08-08:58
"""

from Search_baidu import step
from Search_baidu.open_baidu import Open_baidu
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test001(unittest.TestCase, step.Login):  # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_baidu(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 001
    def test_search_001(self):
        self.assertTrue(self.search())

    # 002
    def test_search_002(self):
        self.assertTrue(self.search())

    # 003
    def test_search_003(self):
        self.assertTrue(self.search())

    # 004
    def test_search_004(self):
        self.assertTrue(self.search())

    # 005
    def test_search_005(self):
        self.assertTrue(self.search())

    # 006
    def test_search_006(self):
        self.assertTrue(self.search())

    # 007
    def test_search_007(self):
        self.assertTrue(self.search())

    # 008
    def test_search_008(self):
        self.assertTrue(self.search())

    # 009
    def test_search_009(self):
        self.assertTrue(self.search())

    # 010
    def test_search_010(self):
        self.assertTrue(self.search())

    # 011
    def test_search_011(self):
        self.assertTrue(self.search())

    # 012
    def test_search_012(self):
        self.assertTrue(self.search())

    # 013
    def test_search_013(self):
        self.assertTrue(self.search())

    # 014
    def test_search_014(self):
        self.assertTrue(self.search())

    # 015
    def test_search_015(self):
        self.assertTrue(self.search())

    # 016
    def test_search_016(self):
        self.assertTrue(self.search())

    # 017
    def test_search_017(self):
        self.assertTrue(self.search())

    # 018
    def test_search_018(self):
        self.assertTrue(self.search())

    # 019
    def test_search_019(self):
        self.assertTrue(self.search())

    # 020
    def test_search_020(self):
        self.assertTrue(self.search())

    # 021
    def test_search_021(self):
        self.assertTrue(self.search())

    # 022
    def test_search_022(self):
        self.assertTrue(self.search())

    # 023
    def test_search_023(self):
        self.assertTrue(self.search())

    # 024
    def test_search_024(self):
        self.assertTrue(self.search())

    # 025
    def test_search_025(self):
        self.assertTrue(self.search())

    # 026
    def test_search_026(self):
        self.assertTrue(self.search())

    # 027
    def test_search_027(self):
        self.assertTrue(self.search())

    # 028
    def test_search_028(self):
        self.assertTrue(self.search())

    # 029
    def test_search_029(self):
        self.assertTrue(self.search())

    # 030
    def test_search_030(self):
        self.assertTrue(self.search())