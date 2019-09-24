# coding=utf-8

"""
Created on 2018年9月4日

@author: Duke    游客模式
"""

from appium_test.PO import base_page
from appium_test.PO import excel
import time


class Tourist(base_page.Action):

    # 1、以游客模式登录首页
    def home_page(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页按钮
        return self.find_item('离家') and self.find_item('睡觉') and self.find_item('起床') and self.find_item(
            '就餐')  # 随机查找4个默认的场景名称

    # 2、以游客模式点击消息中心
    def base_img_right(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页按钮
        self.driver.find_element_by_id(excel.id_con('base_img_right')).click()  # 点击小铃铛
        return self.wait_ac(excel.activity_con('signin_activity'))  # 验证是否进入登陆页面

    # 3、以游客模式点击场景
    def click_the_scene(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_xpath(excel.xpath_con('home')).click()  # 点击首页按钮
        self.find_id('cc.wulian.smarthomev6:id/scene_icon').click()  # 点击场景,场景的ID都一样，测试直接点击通过
        return self.wait_ac(excel.activity_con('signin_activity'))  # 验证是否进入登陆页面

    # 4、以游客模式点击【设备】
    def click_the_device(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备，xpath定位
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 5、以游客模式点击【智能】
    def click_the_find(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_xpath(excel.xpath_con('find')).click()  # 点击智能
        return self.wait_ac(excel.activity_con('signin_activity'))  # 验证是否进入登陆页面

    # 6、以游客模式点击【我的】
    def click_the_mine(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        return self.find_item('物联会员')

    # 7、以游客模式点击【登录/注册】
    def click_the_land(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_account_login_name')).click()
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 8、以游客模式点击【网关中心】
    def click_the_gateway_center(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_gateway_center')).click()
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 9、以游客模式点击【分享管理】
    def click_the_share(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_sharedevice')).click()  # 点击分享管理
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 10、以游客模式点击【物联会员】
    def click_the_member_center(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_member_center')).click()  # 点击物联会员
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 11、以游客模式点击【意见反馈】
    def click_the_customer_feedback(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_customer_feedback')).click()  # 点击意见反馈
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 12、以游客模式点击【设置】
    def click_the_setting(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.find_id(excel.id_con('item_setting')).click()
        return self.wait_ac(excel.activity_con('signin_activity'))

    # 13、以游客模式点击【关于】
    def click_the_about(self):
        self.find_xpath(excel.xpath_con('mine')).click()  # 点击我的按钮
        self.log_out()  # 未登陆则不处理，登陆就退出账号
        self.swipeUp(1000)  # 上划
        self.find_id(excel.id_con('item_about')).click()  # 点击关于
        time.sleep(1)
        return self.find_item('官方网站') and self.find_item('功能介绍') and self.find_item('关于物联')

    # 14、以游客模式点击关于页面【功能介绍】
    def click_the_about_us_introduction(self):
        self.click_the_about()  # 进入关于页面
        self.find_id(excel.id_con('item_about_us_introduction')).click()  # 点击功能介绍
        time.sleep(2)
        return self.find_item('全新风格')

    # 15、以游客模式点击关于页面【关于物联】
    def click_the_about_us_about(self):
        self.click_the_about()  # 进入关于页面
        self.find_id(excel.id_con('item_about_us_about')).click()  # 点击关于物联
        time.sleep(2)
        return self.find_item('南京物联传感技术有限公司')
