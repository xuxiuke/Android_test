# coding=utf-8

"""
Created on 2018年9月18日

@author: Duke    分区管理
"""

from appium_test.PO import base_page
from PO import excel
import time


class Zoning_management(base_page.Action):

    # 1、设备-管理分区，创建分区呵呵，确定
    def new_zoning(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.creat_zone('自动化测试：分区管理001')  # 创建分区
        return self.find_item('自动化测试：分区管理001')

    # 2、设备-管理分区，创建分区哈哈，取消
    def new_zoning_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys('自动化测试：分区管理002')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('自动化测试：分区管理002')

    # 3、设备-管理分区，不输入分区名，确定按钮点击无效，弹窗未消失
    def new_zoning_no_name(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.creat_zone('')  # 创建分区
        return self.find_item('新建分区')

    # 4、设备-管理分区，点击编辑按钮，取消，编辑框消失
    def edit_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        if not self.page_id(excel.id_con('item_area_image_more')):
            self.creat_zone('自动化测试：分区管理004')  # 创建分区
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击分区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_cancel')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('删除')

    # 5、设备-管理分区，点击编辑按钮，删除，确定
    def edit_delete(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.delete_zone_all()  # 删除全部分区
        self.creat_zone('自动化测试：分区管理005')  # 创建分区
        self.delete_zone()  # 删除分区
        return self.find_item('自动化测试：分区管理005')

    # 6、设备-管理分区，点击编辑按钮，删除，取消
    def edit_delete_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.delete_zone_all()  # 删除全部分区
        self.creat_zone('自动化测试：分区管理006')  # 创建分区
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_delete')).click()  # 点击删除按钮
        time.sleep(2)
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('自动化测试：分区管理006')

    # 7、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，确定
    def modify_the_name(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        if not self.page_id(excel.id_con('item_area_image_more')):
            self.creat_zone('自动化测试：分区管理007')  # 创建分区
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_edit')).click()  # 点击修改分区名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'自动化测试：分区管理007—1')
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.find_item('自动化测试：分区管理007—1')

    # 8、设备-管理分区，点击编辑按钮，修改分区名称，输入分区名哈哈，取消
    def modify_the_name_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        if not self.page_id(excel.id_con('item_area_image_more')):
            self.creat_zone('自动化测试：分区管理008')  # 创建分区
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_edit')).click()  # 点击修改分区名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'自动化测试：分区管理008-1')
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(2)
        return self.find_item('自动化测试：分区管理008-1')

    # 9、设备-管理分区，点击编辑按钮，修改分区名称，输入名称为空，确定按钮点击无效，弹窗修改分区还在
    def modify_no_name(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        if not self.page_id(excel.id_con('item_area_image_more')):
            self.creat_zone('自动化测试：分区管理009')  # 创建分区
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_edit')).click()  # 点击修改分区名称
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys('')
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)
        return self.find_item('修改分区')

    # 10、设备-管理分区，创建一个分区，添加一个设备
    def zone_add(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.delete_zone_all()  # 删除全部分区
        self.creat_zone('自动化测试：分区管理010-011')  # 创建分区
        self.find_xpath(excel.xpath_con('first_zone')).click()  # 点击分区
        time.sleep(2)
        self.find_xpath(excel.xpath_con('first_zone_add')).click()  # 点击添加一个设备
        time.sleep(2)
        self.driver.back()
        return self.find_item('1个设备')

    # 11、设备-管理分区，创建一个分区，添加一个设备，再删除一个设备
    def zone_reduce(self):
        self.zone_add()  # 创建一个分区，添加一个设备
        self.find_xpath(excel.xpath_con('first_zone')).click()  # 点击分区
        time.sleep(2)
        self.find_xpath(excel.xpath_con('first_zone_reduce')).click()  # 点击删除一个设备
        time.sleep(2)
        self.driver.back()
        return self.find_item('0个设备')

    # 12、设备-管理分区，创建一个分区，点击设备-全部分区可以找到
    def new_zoning_devide(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.delete_zone_all()  # 删除全部分区
        self.creat_zone('自动化测试：分区管理012-013')  # 创建分区
        self.driver.back()  # 返回设备列表
        time.sleep(1)
        self.find_id(excel.id_con('tv_differentiate_by_area')).click()  # 点击全部分区
        time.sleep(1)
        return self.find_item('自动化测试：分区管理012-013')

    # 13、设备-管理分区，创建一个分区，删除分区，点击设备-全部分区找不到
    def new_zoing_delete_devide(self):
        self.new_zoning_devide()
        self.find_xpath(excel.xpath_con('whole')).click()  # 点击全部
        time.sleep(1)
        self.find_id(excel.id_con('zone_manage')).click()  # 点击左上分区管理按钮
        time.sleep(1)
        self.wait_ac(excel.activity_con('area_activity'))  # 进入管理分区页面
        self.delete_zone()  # 删除分区
        self.driver.back()
        time.sleep(1)
        self.find_id(excel.id_con('tv_differentiate_by_area')).click()  # 点击全部分区
        time.sleep(1)
        return self.find_item('自动化测试：分区管理012-013')

    # 14、设备-管理分区，没有分区
    def no_zone(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.delete_zone_all()  # 删除全部分区
        return self.find_item('暂无分区，点击右上角图标添加吧')

    # 15、设备-管理分区，点击顺序跳转按钮
    def order_adjustment(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.zone_manage_page()  # 进入分区管理页面
        self.find_id(excel.id_con('img_right1')).click()  # 点击顺序调整按钮
        time.sleep(1)
        return self.find_item('顺序调整')
