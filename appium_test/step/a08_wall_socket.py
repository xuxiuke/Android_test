# coding=utf-8

"""
Created on 2018年9月19日

@author: Duke    墙面插座+场景
"""

from appium_test.PO import base_page
from PO import excel
import time

class Wall_socket(base_page.Action):

    # 前置条件：墙面插座详情页，关闭状态
    def closed_state(self):
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.find_text('墙面插座').click()  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item(u'已开启'):
            self.find_xpath(excel.xpath_con('socket_button')).click()
            time.sleep(2)

    # 前置条件：墙面插座详情页，打开状态
    def opened_state(self):
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.find_text('墙面插座').click()  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item(u'已关闭'):
            self.find_xpath(excel.xpath_con('socket_button')).click()
            time.sleep(2)

    # 1、设备，进入墙面插座详情页
    def details_page(self):
        self.old_gateway_mine()  # 账号登陆，我的
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.find_text('墙面插座').click()  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        if self.find_item(u'已开启'):
            return True
        elif self.find_item(u'已关闭'):
            return True
        else:
            return False

    # 2、设备-插座详情页，点击返回按钮，返回设备列表页面
    def details_page_back(self):
        self.details_page()  # 进入设备详情页
        self.find_xpath(excel.xpath_con('back')).click()  # 点击返回按钮
        time.sleep(1)
        return self.find_item('全部类别')  # 确认返回设备列表页面，找全部分区也可

    # 3、设备-插座详情页，关闭状态，点击开关按钮，打开插座
    def open_socket(self):
        self.old_gateway_mine()  # 账号登陆，我的
        self.closed_state()  # 进入设备详情页，关闭状态
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        return self.find_item(u'已开启')

    # 4、设备-插座详情页，打开状态，点击开关按钮，关闭插座
    def close_socket(self):
        self.old_gateway_mine()  # 账号登陆，我的
        self.opened_state()  # 进入设备详情页，打开状态
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        return self.find_item(u'已关闭')

    # 5、设备-插座详情页，点击更多按钮，进入更多页面
    def more_pages(self):
        self.details_page()  # 进入设备详情页
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        return self.find_item('删除设备')

    # 设备-插座详情页-更多，点击返回按钮，进入设备详情页
    def more_pages_back(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_item('已关闭')

    # 设备-插座详情页-更多，重命名哈哈123-确定,toast：修改设备名称成功
    def rename(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'哈哈')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('修改设备名称成功')

    # 设备-插座详情页-更多，重命名哈哈123-确定，返回设备列表，可以查找到新设备名称
    def rename_back(self):
        self.rename()  # 修改名称
        time.sleep(1)
        self.driver.back()  # 点击返回
        time.sleep(1)
        self.driver.back()  # 点击返回
        time.sleep(1)
        for i in range(3):  # 设备多的情况需要调整。。。。。。
            self.swipeDown(1000)
        return self.find_item('哈哈')

    # 设备-插座详情页-更多，重命名哈哈123-取消
    def rename_cancel(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'哈哈')  # 输入新名称
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        return self.find_item('墙面插座')

    # 设备-插座详情页-更多，命名已有的设备名称，toast提示：设备名称重复！加zzz最后运行！
    def zzz_rename_repeat(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'名称重复')  # 输入名称重复
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_toast('设备名称重复！')

    # 设备-插座详情页-更多，重命名-不输入名称，确定按钮点击无效，重命名弹窗还在，查找：请输入设备名
    def rename_none(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_rename')).click()  # 点击重命名
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys('')  # 不输入名称
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        return self.find_item('请输入设备名')

    # 设备-插座详情页-更多，点击分区，进入分区页面
    def zone_pages(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        return self.find_item('未分区')

    # 设备-插座详情页-更多-分区，点击返回按钮，返回更多页面
    def zone_pages_back(self):
        self.zone_pages()  # 进入分区页面
        self.find_id(excel.id_con('img_left')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.find_item('更多')

    # 设备-插座详情页-更多，前置条件至少有一个分区，点击分区，返回更多页面，toast：修改设备区域成功
    def modify_zone(self):
        self.least_one_zone()  # 前置条件，至少一个分区，设备列表页面
        time.sleep(1)
        self.click_device(u'墙面插座')  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_area')).click()  # 点击分区
        time.sleep(1)
        self.find_xpath(excel.xpath_con('more_first_zone')).click()  # 点击第一个分区
        return self.find_toast('修改设备区域成功')

    # 设备-插座详情页-更多，点击未分区，返回更多页面，未分区可以查找到
    def non_zone(self):
        self.zone_pages()
        self.find_xpath(excel.xpath_con('no_zone')).click()  # 点击未分区
        time.sleep(2)
        return self.find_item('未分区')

    # 设备-插座详情页-更多-分区，点击右上管理分区，进入分区管理页面
    def zoning_pages(self):
        self.zone_pages()
        self.find_id(excel.id_con('btn_right')).click()  # 点击右上管理分区按钮
        time.sleep(1)
        return self.find_item('分区管理')

    # 设备-插座详情页-更多-分区-分区管理，点击返回按钮，返回分区页面
    def zoning_pages_back(self):
        self.zoning_pages()  # 进入分区管理页面
        self.find_id(excel.id_con('img_left')).click()  # 点击返回按钮
        return self.find_item('未分区')

    # 设备-插座详情页-更多，点击设备信息，进入设备信息页面，产品名称
    def device_information(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_info')).click()  # 点击设备信息
        time.sleep(1)
        return self.find_item('产品名称')

    # 设备-插座详情页-更多-设备信息，点击返回按钮，返回更多页面
    def device_information_back(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_info')).click()  # 点击设备信息
        time.sleep(1)
        self.find_id(excel.id_con('img_left')).click()  # 点击返回
        time.sleep(1)
        return self.find_item('更多')

    # 设备-插座详情页-更多，点击找设备，弹窗设备指示灯将闪烁10秒
    def find_device(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_find')).click()  # 点击找设备
        time.sleep(1)
        return self.find_item('设备指示灯将闪烁10秒')

    # 设备-插座详情页-更多-找设备弹窗，点击已找到，弹窗消失
    def find_device_found(self):
        self.find_device()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击已找到
        time.sleep(1)
        return self.find_item('设备指示灯将闪烁10秒')

    # 设备-插座详情页-更多-找设备弹窗，点击再闪一次，弹窗还在
    def find_device_find(self):
        self.find_device()  # 找设备弹窗
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击再找一次
        time.sleep(1)
        return self.find_item('设备指示灯将闪烁10秒')

    # 设备-插座详情页-更多，点击日志，日志消息页面
    def log_message_pages(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.wait_ac(excel.activity_con('message_log_activity'))

    # 设备-插座详情页-更多-日志消息，点击返回，返回更多页面
    def log_message_pages_back(self):
        self.log_message_pages()  # 日志消息页面
        self.find_id(excel.id_con('img_left')).click()  # 点击返回按钮
        time.sleep(1)
        return self.find_item('更多')

    # 设备-插座详情页-更多-日志消息，点击按日期查找，弹窗查找编辑框
    def log_search_by_time(self):
        self.log_message_pages()  # 日志消息页面
        self.find_id(excel.id_con('log_image_arrow')).click()  # 点击按日期查找
        time.sleep(3)
        # return self.is_element('xpath', excel.xpath_con('by_date_edit'))  # 判断元素是否存在

    # 设备-插座详情页-更多-日志消息，点击清空日志按钮，弹窗确定清空该设备消息记录
    def emptying_record(self):
        self.log_message_pages()  # 日志消息页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        return self.find_item('确定清空该设备消息记录')

    # 设备-插座详情页-更多-日志消息-清空弹窗，点击取消，弹窗消失
    def emptying_record_cancel(self):
        self.log_message_pages()  # 日志消息页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('确定清空该设备消息记录')

    # 设备-插座详情页-更多-日志消息-清空弹窗，点击确定，弹窗消失，返回更多页面
    def emptying_record_sure(self):
        self.log_message_pages()  # 日志消息页面
        self.find_id(excel.id_con('btn_right')).click()  # 点击清空记录
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.find_item('更多')

    # 设备-插座详情页-更多-日志消息-清空弹窗，清空消息，再返回日志页面，提示：没有日志消息
    def log_emptying(self):
        self.emptying_record_sure()  # 日志消息清空完成，更多页面
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('没有日志消息')

    # 设备-插座详情页-更多-日志消息-清空弹窗，清空消息，再返返回设备详情页，点击两次开关按钮，再进日志页面，查到已打开
    def log_open(self):
        self.emptying_record_sure()  #  清空日志消息，更多页面
        self.driver.back()
        time.sleep(1)
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已打开')

    # 设备-插座详情页-更多-日志消息-清空弹窗，清空消息，再返返回设备详情页，点击两次开关按钮，再进日志页面，查到已关闭
    def log_close(self):
        self.emptying_record_sure()  #  清空日志消息，更多页面
        self.driver.back()
        time.sleep(1)
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('socket_button')).click()  # 点击开关按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('more')).click()  # 点击右上更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_root')).click()  # 点击日志
        time.sleep(2)
        return self.find_item('已关闭')

    # 设备-插座详情页-更多，点击删除设备，弹窗确定删除设备吗？
    def delete_device(self):
        self.more_pages()  # 进入更多页面
        time.sleep(1)
        self.find_id(excel.id_con('item_device_more_delete')).click()  # 点击删除设备按钮
        time.sleep(1)
        return self.find_item('确定删除设备吗？')

    # 设备-插座详情页-更多-删除设备弹窗，点击取消按钮，弹窗消失（删除设备用例省略）
    def delete_device_cancel(self):
        self.delete_device()  # 删除设备
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('确定删除设备吗？')

    # 场景，设置场景打开插座    --------------------------------------------------------------
    def scene_open_socket(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.switch_h5()  # 切换到H5页面
        self.find_xpath(excel.xpath_con('socket_scene')).click()  # 点击墙面插座
        time.sleep(1)
        self.switch_app()  # 切回原生
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        return self.find_item('呵呵123')

    # 关闭插座，点击打开插座场景
    def click_scene_open_socket(self):
        self.scene_open_socket()  # 设置场景，打开插座
        self.driver.back()  # 返回首页
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'墙面插座')  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        time.sleep(2)
        if self.find_item(u'已开启'):
            self.find_xpath(excel.xpath_con('socket_button')).click()  # 关闭插座
        time.sleep(1)
        self.driver.back()
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('text(\"呵呵123\")').click()  # 点击场景-呵呵123
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'墙面插座')  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        return self.find_item('已开启')

    # 场景，设置场景关闭插座
    def scene_close_socket(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'哈哈123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.switch_h5()  # 切换到H5页面
        self.find_xpath(excel.xpath_con('socket_scene')).click()  # 点击墙面插座
        time.sleep(1)
        self.switch_app()  # 切回原生
        self.find_xpath(excel.xpath_con('socket_close')).click()  # 点击关
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        return self.find_item('哈哈123')

    # 打开插座，点击关闭插座场景
    def click_scene_close_socket(self):
        self.scene_close_socket()  # 设置场景，关闭插座
        self.driver.back()  # 返回首页
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'墙面插座')  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        time.sleep(2)
        if self.find_item(u'已关闭'):
            self.find_xpath(excel.xpath_con('socket_button')).click()  # 开启插座
        time.sleep(1)
        self.driver.back()
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator('text(\"哈哈123\")').click()  # 点击场景-哈哈123
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.click_device(u'墙面插座')  # 点击墙面插座
        self.wait_ac(excel.activity_con('device_detail_activity'))
        return self.find_item('已关闭')

    # 场景，添加延时页面，点击延时按钮，弹出延时设置编辑框
    def scene_time(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.switch_h5()  # 切换到H5页面
        self.find_xpath(excel.xpath_con('socket_scene')).click()  # 点击墙面插座
        time.sleep(1)
        self.switch_app()  # 切回原生
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('delay_close')).click()  # 点击打开延时按钮
        time.sleep(1)
        return self.find_item('秒')
        # return self.is_element('xpath', excel.xpath_con('second_1'))  # 判断元素是否存在

    # 场景，添加延时页面，点击延时按钮，弹出延时设置编辑框，再次点击延时按钮，编辑框隐藏
    def scene_time_off(self):
        self.scene_time()  # 场景，打开延时开关
        self.find_xpath(excel.xpath_con('delay_open')).click()  # 点击关闭延时开关
        time.sleep(1)
        return self.find_item('秒')

    # 场景，添加延时页面，设置延时任务，编辑场景页面查找？秒后执行
    def scene_delay(self):
        self.scene_time()  # 场景，打开延时开关
        self.tap_scene_delay()  # 点击坐标，增加1s
        self.tap_scene_delay()  # 点击坐标，增加1s
        self.tap_scene_delay()  # 点击坐标，增加1s
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        time.sleep(1)
        return self.find_item('3秒后执行')

    # 场景，设置场景打开插座，点击返回按钮，弹窗：编辑的场景尚未保存，是否退出
    def editscene_back(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.switch_h5()  # 切换到H5页面
        self.find_xpath(excel.xpath_con('socket_scene')).click()  # 点击墙面插座
        time.sleep(1)
        self.switch_app()  # 切回原生
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_goback')).click()  # 点击左上返回按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('editScene_leave_scene'))  # 判断弹窗元素是否存在

    # 场景，设置场景打开插座，点击返回按钮，点击取消，弹窗消失
    def editscene_back_cancel(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_xpath(excel.xpath_con('editScene_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('editScene_leave_scene'))  # 判断弹窗元素是否存在

    # 场景，设置场景打开插座，点击返回按钮，点击退出，任务未保存
    def editscene_back_exit(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_xpath(excel.xpath_con('editScene_leave')).click()  # 点击退出按钮
        time.sleep(1)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_edit')).click()  # 点击编辑场景
        time.sleep(1)
        return self.find_item('墙面插座')

    # 场景，设置场景打开插座，点击返回按钮，点击保存并退出，任务保存成功
    def editscene_back_exitsave(self):
        self.editscene_back()  # 场景编辑页面，编辑的场景尚未保存弹窗
        self.find_xpath(excel.xpath_con('editScene_leave_save')).click()  # 点击退出保存按钮
        time.sleep(2)
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_edit')).click()  # 点击编辑场景
        time.sleep(1)
        return self.find_item('墙面插座')

    # 场景，设置场景打开插座，左划拉出删除按钮
    def editscene_delete(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.switch_h5()  # 切换到H5页面
        self.find_xpath(excel.xpath_con('socket_scene')).click()  # 点击墙面插座
        time.sleep(1)
        self.switch_app()  # 切回原生
        self.find_xpath(excel.xpath_con('socket_open')).click()  # 点击开
        time.sleep(1)
        self.find_xpath(excel.xpath_con('finish_delay')).click()  # 点击右上完成按钮
        time.sleep(2)
        self.leftswip_editscene(2000)
        return self.find_item('删除')

    # 场景，设置场景打开插座，左划拉出删除按钮，点击删除，任务被删除
    def editscene_delete_click(self):
        self.editscene_delete()  # 场景编辑页面，拉出删除按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('ediescene_delete')).click()  # 点击删除按钮
        time.sleep(1)
        return self.find_item('墙面插座')

    # 场景，设置场景打开插座，点击任务，可以重新设置任务，进入设置设备状态页面
    def editscene_edit(self):
        self.scene_open_socket()  # 设置场景，插座打开
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_edit')).click()  # 点击编辑场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editscene_action_list')).click()  # 点击第一个任务
        time.sleep(1)
        return self.find_item('设置设备状态')

    # 场景，添加设备页面，点击全部分区，拉出所有分区，查找xpath全部分区元素
    def editscene_allzone(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device_list_allAreas')).click()  # 点击全部分区
        time.sleep(1)
        return self.is_element('xpath', excel.xpath_con('all_zone'))  # 验证全部分区元素是否存在

    # 场景，添加设备页面，点击全部类别，拉出所有类别，查找智能门锁
    def editscene_allcategory(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device_list_Categories')).click()  # 点击全部分类
        time.sleep(1)
        return self.find_item('智能门锁')

    # 场景，添加设备页面，点击批量添加，进入批量添加页面，查找全选
    def editscene_batchadd(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'呵呵123')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('editScene_add_equipment')).click()  # 点击添加任务按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('batchAdd')).click()  # 点击批量添加
        time.sleep(1)
        return self.find_item('全选')
