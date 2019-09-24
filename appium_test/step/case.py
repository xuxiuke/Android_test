# coding=utf-8

"""
Created on 2018年11月07日

@author: Duke    添加多个场景和区域
"""

from appium_test.PO import base_page
from PO import excel
import time

class Case(base_page.Action):

    # 添加16个场景，1-16
    def add_scene(self):
        self.scene_page()  # 全部场景页面，删除已有场景
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'1')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'2')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'3')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'4')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'5')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'6')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'7')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'8')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'9')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'10')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'11')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'12')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'13')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'14')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'15')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        self.wait_ac(excel.activity_con('add_scence_activity'))  # 场景名称与图标页面
        time.sleep(1)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(u'16')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_sure')).click()  # 点击确定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('finishScene')).click()  # 点击保存按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面

    # 添加ABCDEFGHUJKLMNOP区域
    def add_zone(self):
        self.zoning_management_page()  # 分区管理页面，删除已有分区
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'A')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'B')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'C')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'D')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'E')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'F')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'G')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'H')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'I')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'J')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'K')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'L')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'M')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'N')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'O')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(u'P')  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)
