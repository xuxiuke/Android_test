# coding=utf-8

"""
Created on 2018年11月01日

@author: Duke    门窗磁探测器
"""

from appium_test.PO import base_page
from PO import excel
import time

class Magnetic(base_page.Action):
    # 前置条件，设防中
    def fortification(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'门窗磁探测器')  # 点击门窗磁探测器
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item('已撤防'):
            self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮

    # 前置条件，已撤防
    def withdrawn(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'门窗磁探测器')  # 点击门窗磁探测器
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item('设防中'):
            self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮

    # 设备列表，点击门窗磁探测器，进入详情页
    def magnetic_page(self):
        self.old_gateway()  # 账号登陆，网关绑定
        self.driver.back()  # 返回我的页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'门窗磁探测器')  # 点击门窗磁探测器
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item('设防中'):
            return True
        elif self.find_item('已撤防'):
            return True
        else:
            return False

    # 设备详情页，点击左上返回按钮，返回设备列表
    def magnetic_page_back(self):
        self.magnetic_page()  # 门窗磁探测器详情页
        self.find_xpath(excel.xpath_con('magnetic_back')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_item('搜索设备')

    # 设备详情页-设防中，点击撤防按钮，变成已撤防
    def fortification_click(self):
        self.fortification()  # 设防中
        time.sleep(1)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(1)
        return self.find_item('已撤防')

    # 设备详情页-设防中，可以查找到正常(门窗磁闭合状态)
    def fortification_normal(self):
        self.fortification()  # 设防中
        time.sleep(1)
        if self.find_item('正常'):
            return True
        else:
            return False

    # 设备详情页-已撤防，点击设防按钮，变成设防中
    def withdrawn_click(self):
        self.withdrawn()  # 已撤防
        time.sleep(1)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(1)
        return self.find_item('设防中')

    # 设备详情页-已撤防，查不到正常(门窗磁闭合状态)
    def withdrawn_normal(self):
        self.withdrawn()  # 已撤防
        time.sleep(1)
        if self.find_item('正常'):
            return True
        else:
            return False

    # 设备详情页，点击更多按钮，进入更多页面,查找删除设备按钮元素
    def more_page(self):
        self.magnetic_page()  # 设备详情页
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面，点击左上返回按钮，返回设备详情页
    def more_page_back(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('magnetic_button'))  # 验证页面是否有设防/撤防按钮

    # 更多页面，点击重命名，重命名弹窗
    def rename(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证重命名弹窗是否存在

    # 更多页面-重命名弹窗，输入新名称呵呵123，点击取消按钮，弹窗消失，名称未修改
    def rename_cancel(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵123')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('呵呵123')

    # 更多页面-重命名弹窗，输入新名称呵呵123，点击确定按钮，弹窗消失，名称修改为呵呵123,toast：修改设备名称成功
    def rename_sure(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵123')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('修改设备名称成功')

    # 更多页面-重命名弹窗，不输入名称，点击确定无效，查找：请输入设备名
    def rename_none(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys('')  # 不输入名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_item('请输入设备名')

    # 重命名设备名称，再次设置设备名称为呵呵123，toast提示：设备名称重复！
    def rename_repeat(self):
        self.rename()  # 重命名弹窗
        self.find_id(excel.id_con('et_user_info')).send_keys(u'名称重复')  # 输入名称重复
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('设备名称重复！')

    # 更多页面，点击分区，进入分区页面
    def zone_page(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('no_zone'))  # 验证页面是否有未分区元素

    # 更多页面-分区页面，点击左上返回按钮，返回更多页面
    def zone_page_back(self):
        self.zone_page()  # 更多，分区页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-分区页面，前置条件至少有一个分区，点击分区，返回更多页面，toast：修改设备区域成功
    def change_zone(self):
        self.least_one_zone()  # 至少一个分区
        time.sleep(1)
        self.click_device(u'门窗磁探测器')  # 点击门窗磁探测器
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more_first_zone')).click()  # 点击第一个分区
        return self.find_toast('修改设备区域成功')

    # 更多页面-分区页面，点击未分区，返回更多页面，未分区可以查找到
    def zone_page_non(self):
        self.zone_page()  # 更多，分区页面
        self.find_xpath(excel.xpath_con('no_zone')).click()  # 点击未分区
        time.sleep(2)
        return self.find_item('未分区')

    # 更多页面-分区页面，点击右上管理分区，进入分区管理页面
    def zone_manage_page(self):
        self.zone_page()  # 更多，分区页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击管理分区
        time.sleep(1)
        return self.find_item('分区管理')

    # 更多页面-分区页面-管理分区页面，点击返回按钮，返回分区页面
    def zone_manage_page_back(self):
        self.zone_manage_page()  # 分区管理页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('no_zone'))  # 验证页面是否有未分区元素

    # 更多页面，点击设备信息，进入设备信息页面
    def device_information(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_info')).click()  # 点击设备信息
        time.sleep(1)
        return self.find_item('产品名称')

    # 更多页面-设备信息页面，点击左上返回按钮，返回更多页面
    def device_information_back(self):
        self.device_information()  #  设备信息页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面，点击找设备，弹出设备指示灯将闪烁10秒弹窗
    def finddevice(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_find')).click()  # 点击找设备
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面-设备指示灯将闪烁10秒弹窗，点击已找到，弹窗消失
    def finddevice_found(self):
        self.finddevice()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击已找到
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面-设备指示灯将闪烁10秒弹窗，点击再闪烁一次，弹窗还在
    def finddevice_again(self):
        self.finddevice()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击再闪烁一次
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗是否存在

    # 更多页面，点击报警消息，进入报警消息页面
    def alarm_message_page(self):
        self.more_page()  # 更多页面
        self.find_xpath(excel.xpath_con('more_alarm_message')).click()  # 点击报警消息
        time.sleep(2)
        return self.wait_ac(excel.activity_con('message_alarm_activity'))  # 验证是否进入报警消息页面

    # 更多页面-报警消息页面，点击左上返回按钮，返回更多页面
    def alarm_message_page_back(self):
        self.alarm_message_page()  # 报警消息页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-报警消息页面，点击按日期查找，弹出日期编辑
    def alarm_by_date(self):
        self.alarm_message_page()  # 报警消息页面
        self.find_id(excel.id_con('log_text_date')).click()  # 点击按日期查找
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 验证页面是否有日期编辑框元素

    # 更多页面-报警消息页面，点击按日期查找，弹出日期编辑，再次点击，编辑框隐藏
    def alarm_by_date_hide(self):
        self.alarm_by_date()  # 弹出按日期查找编辑框
        # self.switch_h5()  # 切换到H5页面
        # self.driver.swipe(500, 1600, 500, 1600, 500)
        # self.driver.tap([(138, 1846), (282, 1911)], 500)  # 点击按日期查找区域以外任何地方(代码无效)
        # self.switch_app()  # 切回原生
        self.driver.back()
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 验证页面是否有日期编辑框元素

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗
    def alarm_empty(self):
        self.alarm_message_page()  # 报警消息页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失
    def alarm_empty_cancel(self):
        self.alarm_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-报警消息页面，点击右上清空记录，弹出清空记录弹窗，点击确定按钮，弹窗消失，消息记录清空，自动返回更多页面
    def alarm_empty_sure(self):
        self.alarm_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-报警消息页面-清空记录，再次进入报警记录页面，提示：没有报警消息
    def alarm_empty_sure_again(self):
        self.alarm_empty_sure()  # 清空记录
        self.find_xpath(excel.xpath_con('more_alarm_message')).click()  # 点击报警消息
        time.sleep(1)
        return self.find_item('没有报警消息')

    # 更多页面，点击日志，进入日志页面
    def log_page(self):
        self.more_page()  # 更多页面
        self.find_xpath(excel.xpath_con('more_log')).click()  # 点击日志
        time.sleep(2)
        return self.wait_ac(excel.activity_con('message_log_activity'))  # 验证是否进入日志页面

    # 更多页面-日志页面，点击左上返回按钮，返回更多页面
    def log_page_back(self):
        self.log_page()  # 日志页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-日志页面，点击按日期查找，弹出日期编辑
    def log_by_date(self):
        self.log_page()  # 日志页面
        self.find_id(excel.id_con('log_text_date')).click()  # 点击按日期查找
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 验证页面是否有日期编辑框元素

    # 更多页面-日志页面，点击按日期查找，弹出日期编辑，再次点击，编辑框隐藏
    def log_by_date_hide(self):
        self.log_by_date()  # 按日期查找编辑框
        self.driver.back()
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 验证页面是否有日期编辑框元素

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗
    def log_empty(self):
        self.log_page()  # 日志页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失
    def log_empty_cancel(self):
        self.log_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面-日志页面，点击右上清空记录，弹出清空记录弹窗，点击取消按钮，弹窗消失，消息记录清空，自动返回更多页面
    def log_empty_sure(self):
        self.log_empty()  # 清空记录弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.is_element('id', excel.id_con('item_device_more_delete'))  # 验证是否有删除设备按钮

    # 更多页面-日志页面-清空记录，再次进入日志页面，提示：没有日志消息
    def log_empty_sure_again(self):
        self.log_empty_sure()  # 清空记录
        self.find_xpath(excel.xpath_con('more_log')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('没有日志消息')

    # 更多页面-日志页面-清空记录，返回详情页点击设防/撤防两次，再次进入日志消息，查找：已设防
    def log_fortification(self):
        self.log_empty_sure()  # 清空记录
        self.driver.back()  # 返回设备详情页
        time.sleep(2)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(3)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more_log')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已设防')

    # 更多页面-日志页面-清空记录，返回详情页点击设防/撤防两次，再次进入日志消息，查找：已撤防
    def log_withdrawn(self):
        self.log_empty_sure()  # 清空记录
        self.driver.back()  # 返回设备详情页
        time.sleep(2)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(3)
        self.find_xpath(excel.xpath_con('magnetic_button')).click()  # 点击设防/撤防按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more_log')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已撤防')

    # 更多页面，点击删除设备按钮，弹出确定弹窗
    def delete_device(self):
        self.more_page()  # 更多页面
        self.find_id(excel.id_con('item_device_more_delete')).click()  # 点击删除设备按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在

    # 更多页面，点击删除设备按钮，弹出确定弹窗，点击取消按钮，弹窗消息（确定按钮测试不做）
    def delete_device_cancel(self):
        self.delete_device()  # 删除设备弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('task_not_empty'))  # 验证弹窗元素是否存在
