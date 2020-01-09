# coding=utf-8

"""
Created on 2018年8月15日

@author: Duke    公共类
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.mobilecommand import MobileCommand
from appium.webdriver.common.touch_action import TouchAction
from PO import excel
from PIL import Image


class Action(object):
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 屏幕向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)

    # 左划拉出网关解除绑定按钮,换手机需要重新填数据-------------------------
    def left_stroke(self, t):
        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # l = self.getSize()
        self.driver.swipe(850, 550, 300, 550, t)

    # 场景编辑页面，左划拉出删除按钮，换手机需要重新填数据
    def leftswip_editscene(self, t):
        self.driver.swipe(850, 850, 300, 850, t)

    # 我的管家页面，左划，删除管家
    def leftswip_housekeeper(self, t):
        self.driver.swipe(850, 300, 300, 300, t)

    # 定时任务编辑页面，左划，删除执行任务
    def leftswip_delaytask(self, t):
        self.driver.swipe(850, 1000, 300, 1000, t)

    # 情景任务编辑页面-条件任务，左划，拉出删除按钮
    def leftswip_condition(self, t):
        self.driver.swipe(850, 600, 300, 600, t)

    # 情景任务编辑页面-执行任务，左划，拉出删除按钮（未设置条件任务）
    def leftswip_implement(self, t):
        self.driver.swipe(850, 800, 300, 800, t)

    # 场景-延时编辑框，点击增加1s,换手机需要重新填数据-------------------------
    def tap_scene_delay(self):
        self.driver.tap([(597, 828), (810, 915)], 500)  # 点击坐标，增加1s

    # 长按封装,例子：el = self.find_xpath(excel.xpath_con('first_scene'))
    def long_press_custom(self, el):
        TouchAction(self.driver).long_press(el).perform()

    # 重写元素定位的方法
    def find_id(self, loc):
        try:
            return self.driver.find_element_by_id(loc)
        except Exception as e:
            print('报错：', e)
            print("未找到： %s" % loc)
            return False

    def find_xpath(self, loc):
        try:
            return self.driver.find_element_by_xpath(loc)
        except Exception as e:
            print('报错：', e)
            print("未找到： %s" % loc)
            return False

    def find_text(self, loc):
        try:
            return self.driver.find_element_by_android_uiautomator('text(\"%s\")' % loc)
        except Exception as e:
            print('报错：', e)
            print("未找到： %s" % loc)
            return False

    def find_content_desc(self, loc):
        try:
            return self.driver.find_element_by_accessibility_id(loc)
        except Exception as e:
            print('报错：', e)
            print("未找到： %s" % loc)
            return False

    # 输入验证码1-6
    def input_validation_code(self):
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(11)

    # 输入错误验证码
    def input_error_validation_code(self):
        self.driver.press_keycode(8)
        self.driver.press_keycode(9)
        self.driver.press_keycode(10)
        self.driver.press_keycode(14)

    # 获取控件颜色，颜色正确返回Ture
    def get_colour_text(self, loc):
        fix_rgba = (38, 196, 128)  # 按钮颜色
        els = self.driver.find_elements_by_android_uiautomator('text(\"%s\")' % loc)
        self.driver.get_screenshot_as_file("D:\\test\\appium_test\date\\temp.png")
        pig = Image.open("D:\\test\\appium_test\date\\temp.png")
        for el in els:
            x1 = el.location.get("x")
            y1 = el.location.get("y")
            h = el.size.get("height")
            w = el.size.get("width")
            x2 = x1 + w
            y2 = y1 + h
            el_img = pig.crop(box=(x1, y1, x2, y2))
            el_rgba = el_img.getpixel((0, 0))  # 选取一个像素点
            pig.close()  # 关闭打开的图片
            print('控件色值为：' + el_rgba)  # (38, 196, 128) (216, 216, 216)
            if el_rgba == fix_rgba:
                return True

    # 判断页面上text是否存在
    def find_item(self, text):
        source = self.driver.page_source
        # source = self.driver.current_context
        if text in source:
            print('找到: ' + text)
            return True
        else:
            print('未找到: ' + text)
            return False

    # 判断是否是包涵这个ID的页面
    def page_id(self, id1):
        if self.find_id(id1):
            print('页面包涵ID： ' + id1)
            return True
        else:
            print('页面没有ID： ' + id1)
            return False

    # 获取控件的text
    def get_text(self, id1):
        return self.find_id(id1).text

    # 判断toast是否存在
    def find_toast(self, message):
        try:
            toast_loc = ("xpath", ".//*[contains(@text, '%s')]" % message)
            WebDriverWait(self.driver, 17).until(EC.presence_of_all_elements_located(toast_loc))
            print('找到toast： ' + message)
            return True
        except Exception as e:
            print(e, '未找到toast： ' + message)
            return False

    # 等待activity
    def wait_ac(self, activityName):
        s = self.driver.wait_activity(activityName, 3)
        if s:
            print('找到页面： ' + activityName)
            return True
        else:
            print('未找到页面： ' + activityName)
            return False

    # 设备列表页面点击设备???
    def click_device(self, deviceName):
        for i in range(10):
            if self.find_item(deviceName):
                time.sleep(1)
                self.driver.find_element_by_android_uiautomator('text(\"%s\")' % deviceName).click()
                break
            else:
                self.swipeUp(1000)
                time.sleep(1)

    # 切换至H5界面
    def switch_h5(self):
        print(self.driver.contexts)
        d = self.driver.contexts
        # print (self.driver.current_context)
        # print (self.driver.page_source)  # 打印H5源码
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": d[-1]})
        # self.driver.switch_to.context('WEBVIEW_cc.wulian.smarthomev6')
        # print (self.driver.page_source)  # 打印H5源码
        print(self.driver.current_context)

    # 切换至原生
    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})
        print(self.driver.current_context)

    # self.driver.implicitly_wait(30)  # 智能等待时间

    # ------------------------------------------------------------------------------------------------------------------
    # 前置条件：未登陆则不处理，登陆就退出账号
    def log_out(self):
        text = self.get_text(excel.id_con('item_account_login_name'))  # 获取账户名称
        print('账号昵称： ' + text)
        if text != '登录/注册':
            self.find_id(excel.id_con('item_setting')).click()
            time.sleep(1)
            self.find_id(excel.id_con('item_setting_logout')).click()
            time.sleep(2)

    # 前置条件：账号登陆，我的页面
    def account_login(self):
        self.find_text('我的').click()
        if self.find_text('登录/注册'):
            self.login_accountnumber_password('18013986382', 'wl123456789')  # 登陆账号180
            time.sleep(2)
            self.find_text('我的').click()

    # 前置条件：账号登陆，解绑所有网关，我的页面
    def untie(self):
        self.account_login()  # 登陆
        self.find_id(excel.id_con('item_gateway_center')).click()  # 点击网关中心
        time.sleep(2)
        while True:
            text = self.get_text(excel.id_con('item_gateway_center_name'))  # 获取网关中心网关名
            print('网关名称： ' + text)
            if text != '未登录网关':  # 确保账号没有绑定网关
                self.find_id(excel.id_con('item_gateway_center_list')).click()  # 点击网关列表
                self.wait_ac(excel.activity_con('gateway_list'))  # 确保进入网关列表页面
                time.sleep(2)
                self.unbound_gateway()  # 解除绑定网关
                self.find_id(excel.id_con('img_left')).click()  # 点击返回按钮
                time.sleep(1)
            else:
                break
        self.find_id(excel.id_con('img_left')).click()
        time.sleep(1)

    # 前置条件：账号登陆，如果未绑定网关，绑定网关，网关中心页面
    def old_gateway_center(self):
        self.account_login()  # 登陆
        self.find_id(excel.id_con('item_gateway_center')).click()  # 点击网关中心
        time.sleep(2)
        text = self.get_text(excel.id_con('item_gateway_center_name'))  # 获取网关中心网关名
        print('网关名称： ' + text)
        if text == '未登录网关':
            self.find_id(excel.id_con('item_gateway_center_list')).click()  # 点击网关列表
            self.wait_ac(excel.activity_con('gateway_list'))  # 确保进入网关列表页面
            self.binding_gateway('50294D20B1FC', 'qazwsx1234')  # 绑定网关
            self.driver.back()
            time.sleep(1)

    # 前置条件：账号登陆，如果未绑定网关，绑定网关，我的页面
    def old_gateway_mine(self):
        self.old_gateway_center()  # 账号登陆，网关中心
        self.driver.back()
        time.sleep(2)

    # 前置条件：场景页面，删除全部场景
    def delete_scene_all(self):
        while True:
            if self.page_id(excel.id_con('scene_content')):
                self.delete_scene()  # 删除场景
            else:
                break

    # 前置条件：场景页面，删除场景
    def delete_scene(self):
        self.long_press_custom(self.find_xpath(excel.xpath_con('first_scene')))  # 长按第一个场景
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_scene_text_delete')).click()  # 点击删除
        time.sleep(1)
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)

    # 前置条件：我的页面，进入分区管理页面
    def zone_manage_page(self):
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.find_id(excel.id_con('zone_manage')).click()  # 点击左上分区管理按钮
        time.sleep(2)
        self.wait_ac(excel.activity_con('area_activity'))  # 进入管理分区页面

    # 前置条件：智能-场景页面，创建默认离家场景
    def creat_scene_go_out(self):
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('go_out')).click()  # 点击离家场景图标
        time.sleep(1)
        self.find_content_desc('完成').click()  # 点击完成按钮
        time.sleep(3)
        self.find_content_desc('保存').click()
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面

    # 前置条件：智能-场景页面，创建场景
    def creat_scene(self, name):
        self.find_id(excel.id_con('all_scene_image_add')).click()  # 点击创建场景
        time.sleep(2)
        self.find_xpath(excel.xpath_con('customScene_input_name')).send_keys(name)  # 输入场景名称
        self.find_xpath(excel.xpath_con('motion_mode')).click()  # 点击运动场景图标
        time.sleep(1)
        self.find_content_desc('完成').click()  # 点击完成按钮
        time.sleep(3)
        self.find_content_desc('保存').click()
        self.wait_ac(excel.activity_con('all_scence_activity'))  # 全部场景页面

    # 前置条件：分区管理页面，创建分区
    def creat_zone(self, name):
        self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
        time.sleep(1)
        self.find_id(excel.id_con('et_user_info')).send_keys(name)  # 输入新分区名称，呵呵
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(1)

    # 前置条件：分区管理页面，删除分区
    def delete_zone(self):
        self.find_xpath(excel.xpath_con('item_area_image_more')).click()  # 点击第一个分区更多按钮
        time.sleep(1)
        self.find_id(excel.id_con('popup_edit_area_text_delete')).click()  # 点击删除按钮
        time.sleep(2)
        self.find_id(excel.id_con('dialog_btn_positive')).click()
        time.sleep(1)

    # 前置条件：分区管理页面，删除全部分区
    def delete_zone_all(self):
        while True:
            if self.page_id(excel.id_con('item_area_image_more')):
                self.delete_zone()  # 删除分区
            else:
                break

    # 前置条件，至少有一个分区，设备列表页面???
    def least_one_zone(self):
        self.old_gateway_mine()  # 账号登陆，绑定网关，我的页面
        self.find_xpath(excel.xpath_con('device')).click()  # 点击设备
        time.sleep(1)
        self.find_id(excel.id_con('base_img_right')).click()  # 点击右上+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('device_zone')).click()  # 点击管理分区
        self.wait_ac(excel.activity_con('area_activity'))  # 进入管理分区页面
        if self.page_id(excel.id_con('item_area_image_more')):
            self.driver.back()  # 返回设备列表页面
        else:
            self.find_id(excel.id_con('img_right')).click()  # 点击右键角+按钮，新增分区
            time.sleep(1)
            self.find_id(excel.id_con('et_user_info')).send_keys(u'呵呵')  # 输入新分区名称，呵呵
            self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
            time.sleep(1)
            self.driver.back()  # 返回设备列表页面

    # 前置条件，登陆流程：点击登录/注册-》进入登陆页面-》输入账号-》输入密码-》点击登陆，参数账号和密码
    def login_accountnumber_password(self, accountnumber, password):
        self.find_id(excel.id_con('item_account_login_name')).click()  # 点击登录/注册
        self.wait_ac(excel.activity_con('signin_activity'))  # 进入登陆页面
        self.find_id(excel.id_con('username')).send_keys(accountnumber)
        self.find_id(excel.id_con('password')).send_keys(password)
        self.find_id(excel.id_con('login')).click()

    # 前置条件，绑定网关流程，网关列表页面：点击+按钮-》输入网关账号、密码-》点击绑定按钮
    def binding_gateway(self, number, password):
        self.find_id(excel.id_con('img_right')).click()  # 点击网关列表右上角+按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('et_gateway_username')).send_keys(number)  # 输入网关ID
        self.find_id(excel.id_con('et_gateway_password')).send_keys(password)  # 输入网关密码
        self.find_id(excel.id_con('btn_gateway_login')).click()  # 点击绑定网关按钮
        time.sleep(2)

    # 前置条件，解绑网关流程，网关列表页面：左划网关-》点击解除绑定-》点击确定按钮
    def unbound_gateway(self):
        self.left_stroke(2000)  # 左划拉出解除绑定按钮
        time.sleep(2)
        self.find_xpath(excel.xpath_con('unbind')).click()  # 点击解除绑定按钮
        time.sleep(2)
        self.find_id(excel.id_con('dialog_btn_positive')).click()  # 点击确定按钮
        time.sleep(2)

    # 前置条件，修改网关密码流程，网关中心页面：点击网关设置-》点击修改密码修改-》输入原始密码和新密码-》点击确定按钮
    def modify_gateway_password(self, old, new):
        self.find_id(excel.id_con('item_gateway_center_setting')).click()  # 点击网关设置
        time.sleep(1)
        self.find_id(excel.id_con('item_gateway_setting_info')).click()  # 点击网关密码修改
        time.sleep(1)
        self.find_id(excel.id_con('old_pwd_editText')).send_keys(old)  # 输入原始密码
        self.find_id(excel.id_con('et_new_pwd')).send_keys(new)  # 输入全数字新密码
        time.sleep(2)
        self.find_id(excel.id_con('confirm_pwd_button')).click()  # 点击确定按钮
