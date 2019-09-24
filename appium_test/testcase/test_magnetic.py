#coding=utf-8

"""
Created on 2018年11月01日

@author: Duke    门窗磁探测器    44条用例
"""

from PO.open_app import Open_app
from step import a10_magnetic
import unittest
import time
from PO import excel
@unittest.skip(u'添加场景、区域，跳过测试')
class Test010(unittest.TestCase, a10_magnetic.Magnetic): # TestCase类，所有测试用例类继承的基本类
    """门窗磁探测器"""
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

    # 设备列表，点击门窗磁探测器，进入详情页
    def test_magnetic_page(self):
        self.assertTrue(self.magnetic_page())

    # 设备详情页，点击左上返回按钮，返回设备列表
    def test_magnetic_page_back(self):
        self.assertTrue(self.magnetic_page_back())

    # 设备详情页-设防中，点击撤防按钮，变成已撤防
    def test_fortification_click(self):
        self.assertTrue(self.fortification_click())

    # 设备详情页-设防中，可以查找到正常(门窗磁闭合状态)
    def test_fortification_normal(self):
        self.assertTrue(self.fortification_normal())

    # 设备详情页-已撤防，点击设防按钮，变成设防中
    def test_withdrawn_click(self):
        self.assertTrue(self.withdrawn_click())

    # 设备详情页-已撤防，查不到正常(门窗磁闭合状态)
    def test_withdrawn_normal(self):
        self.assertFalse(self.withdrawn_normal())

    # 设备详情页，点击更多按钮，进入更多页面,查找删除设备按钮元素
    def test_more_page(self):
        self.assertTrue(self.more_page())

    # 更多页面，点击左上返回按钮，返回设备详情页
    def test_more_page_back(self):
        self.assertTrue(self.more_page_back())

    # 更多页面，点击重命名，重命名弹窗
    def test_rename(self):
        self.assertTrue(self.rename())

    # 更多页面-重命名弹窗，输入新名称呵呵123，点击取消按钮，弹窗消失，名称未修改
    def test_rename_cancel(self):
        self.assertFalse(self.rename_cancel())

    # 更多页面-重命名弹窗，输入新名称呵呵123，点击确定按钮，弹窗消失，名称修改为呵呵123,toast：修改设备名称成功
    def test_rename_sure(self):
        self.assertTrue(self.rename_sure())
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'门窗磁探测器')  # 输入原名
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮

    # 更多页面-重命名弹窗，不输入名称，点击确定无效，查找：请输入设备名
    def test_rename_none(self):
        self.assertTrue(self.rename_none())

    # 重命名设备名称，再次设置设备名称为呵呵123，toast提示：设备名称重复！
    def test_rename_repeat(self):
        self.assertTrue(self.rename_repeat())

    # 更多页面，点击分区，进入分区页面
    def test_zone_page(self):
        self.assertTrue(self.zone_page())

    # 更多页面-分区页面，点击左上返回按钮，返回更多页面
    def test_zone_page_back(self):
        self.assertTrue(self.zone_page_back())

    # 更多页面-分区页面，前置条件至少有一个分区，点击分区，返回更多页面，toast：修改设备区域成功
    def test_change_zone(self):
        self.assertTrue(self.change_zone())

    # 更多页面-分区页面，点击未分区，返回更多页面，未分区可以查找到
    def test_zone_page_non(self):
        self.assertTrue(self.zone_page_non())

    # 更多页面-分区页面，点击右上管理分区，进入分区管理页面
    def test_zone_manage_page(self):
        self.assertTrue(self.zone_manage_page())

    # 更多页面-分区页面-管理分区页面，点击返回按钮，返回分区页面
    def test_zone_manage_page_back(self):
        self.assertTrue(self.zone_manage_page_back())

    # 更多页面，点击设备信息，进入设备信息页面
    def test_device_information(self):
        self.assertTrue(self.device_information())

    # 更多页面-设备信息页面，点击左上返回按钮，返回更多页面
    def test_device_information_back(self):
        self.assertTrue(self.device_information_back())

    # 更多页面，点击找设备，弹出设备指示灯将闪烁10秒弹窗
    def test_finddevice(self):
        self.assertTrue(self.finddevice())

    # 更多页面-设备指示灯将闪烁10秒弹窗，点击已找到，弹窗消失
    def test_finddevice_found(self):
        self.assertFalse(self.finddevice_found())

    # 更多页面-设备指示灯将闪烁10秒弹窗，点击再闪烁一次，弹窗还在
    def test_finddevice_again(self):
        self.assertTrue(self.finddevice_again())

    # 更多页面，点击报警消息，进入报警消息页面
    def test_alarm_message_page(self):
        self.assertTrue(self.alarm_message_page())

    # 更多页面-报警消息页面，点击左上返回按钮，返回更多页面
    def test_alarm_message_page_back(self):
        self.assertTrue(self.alarm_message_page_back())

    # 更多页面-报警消息页面，点击按日期查找，弹出日期编辑
    def test_alarm_by_date(self):
        self.assertTrue(self.alarm_by_date())

    # 更多页面-报警消息页面，点击按日期查找，弹出日期编辑，再次点击，编辑框隐藏
    def test_alarm_by_date_hide(self):
        self.assertFalse(self.alarm_by_date_hide())

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗
    def test_alarm_empty(self):
        self.assertTrue(self.alarm_empty())

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失
    def test_alarm_empty_cancel(self):
        self.assertFalse(self.alarm_empty_cancel())

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗，点击确定按钮，弹窗消失，消息记录清空，自动返回更多页面
    def test_alarm_empty_sure(self):
        self.assertTrue(self.alarm_empty_sure())

    # 更多页面-报警消息页面-清空记录，再次进入报警记录页面，提示：没有报警消息
    def test_alarm_empty_sure_again(self):
        self.assertTrue(self.alarm_empty_sure_again())

    # 更多页面，点击日志，进入日志页面
    def test_log_page(self):
        self.assertTrue(self.log_page())

    # 更多页面-日志页面，点击左上返回按钮，返回更多页面
    def test_log_page_back(self):
        self.assertTrue(self.log_page_back())

    # 更多页面-日志页面，点击按日期查找，弹出日期编辑
    def test_log_by_date(self):
        self.assertTrue(self.log_by_date())

    # 更多页面-日志页面，点击按日期查找，弹出日期编辑，再次点击，编辑框隐藏
    def test_log_by_date_hide(self):
        self.assertFalse(self.log_by_date_hide())

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗
    def test_log_empty(self):
        self.assertTrue(self.log_empty())

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失
    def test_log_empty_cancel(self):
        self.assertFalse(self.log_empty_cancel())

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失，消息记录清空，自动返回更多页面
    def test_log_empty_sure(self):
        self.assertTrue(self.log_empty_sure())

    # 更多页面-日志页面-清空记录，再次进入日志页面，提示：没有日志消息
    def test_log_empty_sure_again(self):
        self.assertTrue(self.log_empty_sure_again())

    # 更多页面-日志页面-清空记录，返回详情页点击设防/撤防两次，再次进入日志消息，查找：已设防
    def test_log_fortification(self):
        self.assertTrue(self.log_fortification())

    # 更多页面-日志页面-清空记录，返回详情页点击设防/撤防两次，再次进入日志消息，查找：已撤防
    def test_log_withdrawn(self):
        self.assertTrue(self.log_withdrawn())

    # 更多页面，点击删除设备按钮，弹出确定弹窗
    def test_delete_device(self):
        self.assertTrue(self.delete_device())

    # 更多页面，点击删除设备按钮，弹出确定弹窗，点击取消按钮，弹窗消息（确定按钮测试不做）
    def test_delete_device_cancel(self):
        self.assertFalse(self.delete_device_cancel())

