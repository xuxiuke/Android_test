# coding=utf-8

"""
Created on 2019年04月03日

@author: Duke    分区管理    15条用例
"""

from PO.open_app import Open_app
from step import a06_zoning_management
import unittest
import time
import warnings

class Test006(unittest.TestCase, a06_zoning_management.Zoning_management): # TestCase类，所有测试用例类继承的基本类
    """分区管理测试"""
    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 屏蔽ResourceWarning报警
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、设备-管理分区，创建分区呵呵，确定
    def test_new_zoning(self):
        self.assertTrue(self.new_zoning())

    # 2、设备-管理分区，创建分区哈哈，取消
    def test_new_zoning_cancel(self):
        self.assertFalse(self.new_zoning_cancel())

    # 3、设备-管理分区，不输入分区名，确定按钮不可点击
    def test_new_zoning_no_name(self):
        self.assertTrue(self.new_zoning_no_name())

    # 4、设备-管理分区，点击编辑按钮，取消，编辑框消失
    def test_edit_cancel(self):
        self.assertFalse(self.edit_cancel())

    # 5、设备-管理分区，点击编辑按钮，删除，确定
    def test_edit_delete(self):
        self.assertFalse(self.edit_delete())

    # 6、设备-管理分区，点击编辑按钮，删除，取消
    def test_edit_delete_cancel(self):
        self.assertTrue(self.edit_delete_cancel())

    # 7、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，确定
    def test_modefy_the_name(self):
        self.assertTrue(self.modify_the_name())

    # 8、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，取消
    def test_modefy_the_name_cancel(self):
        self.assertFalse(self.modify_the_name_cancel())

    # 9、设备-管理分区，点击编辑按钮，修改分区名称，输入名称为空，确定按钮点击无效，弹窗修改分区还在
    def test_modefy_no_name(self):
        self.assertTrue(self.modify_no_name())

    # 10、设备-管理分区，创建一个分区，添加一个设备
    def test_zone_add(self):
        self.assertTrue(self.zone_add())

    # 11、设备-管理分区，创建一个分区，添加一个设备，再删除一个设备
    def test_zone_reduce(self):
        self.assertTrue(self.zone_reduce())

    # 12、设备-管理分区，创建一个分区，点击设备-全部分区可以找到
    def test_new_zoning_devide(self):
        self.assertTrue(self.new_zoning_devide())

    # 13、设备-管理分区，创建一个分区，删除分区，点击设备-全部分区找不到
    def test_new_zoning_delete_devide(self):
        self.assertFalse(self.new_zoing_delete_devide())

    # 14、设备-管理分区，没有分区
    def test_no_zone(self):
        self.assertTrue(self.no_zone())

    # 15、设备-管理分区，点击顺序跳转按钮
    def test_order_adjustment(self):
        self.assertTrue(self.order_adjustment())
