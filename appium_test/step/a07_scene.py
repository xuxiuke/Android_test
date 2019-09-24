# coding=utf-8

"""
Created on 2018年9月19日

@author: Duke    场景
"""

from appium_test.PO import base_page
from PO import excel
import time


class Scene(base_page.Action):

    # 1、首页-全部场景，无场景，页面提示：无场景
    def no_scene(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.delete_scene_all()  # 删除全部场景
        return self.find_item('暂无场景')

    # 2、首页-全部场景，创建场景，默认离家名称，场景编辑页面点击保存
    def create_scene_save(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.creat_scene_go_out()  # 创建默认离家场景
        return self.find_item('离家')

    # 3、首页-全部场景，创建场景，默认回家名称，场景编辑页面返回
    def create_scene_back(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('go_home')).click()  # 点击回家场景图标
        time.sleep(1)
        self.find_content_desc('完成').click()  # 点击完成按钮
        time.sleep(3)
        self.driver.back()
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        return self.find_item('回家')

    # 4、首页-全部场景，创建场景，默认睡眠名称，左上返回按钮
    def create_scene_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('go_sleep')).click()  # 点击回家场景图标
        time.sleep(1)
        self.find_content_desc('javascript:;').click()  # 点击左上返回按钮
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面
        return self.find_item('睡眠')

    # 5、首页-全部场景，创建场景自定义名称呵呵123
    def hehe123_scene(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.creat_scene('自动化005')
        return self.find_item('自动化005')

    # 6、首页-全部场景，创建场景，不输入名称，确定点击无效，还在场景名称与图标页面
    def no_name_scene(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('motion_mode')).click()  # 点击运动场景图标
        time.sleep(1)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys('')  # 输入kong场景名称
        self.find_content_desc('完成').click()  # 点击完成按钮
        time.sleep(3)
        return self.find_item('场景名称') and self.find_item('场景图标')

    # 7、首页-全部场景，创建场景，创建相同名称的场景，toast提示：该场景名称已存在，请换一个(H5页面toast获取不到，改用定位还在场景名称与图标页面)
    def same_name_scene(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.creat_scene('自动化007')
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys('自动化007')  # 输入场景名称
        self.find_xpath(excel.xpath_con('motion_mode')).click()  # 点击运动场景图标
        time.sleep(1)
        self.find_content_desc('完成').click()  # 点击完成按钮
        time.sleep(3)
        return self.find_item('场景名称') and self.find_item('场景图标')

    # 8、首页-全部场景，长按场景，取消，编辑框消失
    def longpress_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        if not self.page_id(excel.id_con('scene_content')):  # 如果没有场景就创建一个场景
            self.creat_scene('自动化008')
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_cancel')).click()  # 点击取消
        time.sleep(1)
        return self.find_item('取消')

    # 9、首页-全部场景，长按场景，删除-取消
    def longpress_delete_cancel(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.delete_scene_all()  # 删除所有场景
        self.creat_scene('自动化009')
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_delete')).click()  # 点击删除
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_negative')).click()  # 点击取消按钮
        time.sleep(1)
        return self.find_item('自动化009')

    # 10、首页-全部场景，长按场景，删除-确定
    def longpress_delete(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        self.delete_scene_all()  # 删除所有场景
        self.creat_scene('自动化010')
        self.delete_scene()
        return self.find_item('自动化010')

    # 11、首页-全部场景，长按场景，编辑场景
    def longpress_edit(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能按钮
        time.sleep(1)
        if not self.page_id(excel.id_con('scene_content')):  # 如果没有场景就创建一个场景
            self.creat_scene('自动化011')
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_edit')).click()  # 点击编辑场景
        time.sleep(1)
        return self.find_item('编辑场景') and self.find_item('添加任务')
