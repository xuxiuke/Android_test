#coding=utf-8

"""
作者: Duke
文件名: base.py
创建时间: 2020/04/08-09:04
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.mobilecommand import MobileCommand
from appium.webdriver.common.touch_action import TouchAction
from PIL import Image
from appium.webdriver.connectiontype import ConnectionType


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

    # 获取控件颜色，激活颜色正确返回Ture
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
            print(el_rgba)  # (38, 196, 128) (216, 216, 216)
            if el_rgba == fix_rgba:
                return True

    def get_colour_xpath(self, loc):
        fix_rgba = (38, 196, 128)  # 按钮颜色
        els = self.driver.find_elements_by_xpath(loc)
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
            print(el_rgba)  # (38, 196, 128) (216, 216, 216)
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

    '''
        # WIFI
        ConnectionType.WIFI_ONLY
        # 数据流量
        ConnectionType.DATA_ONLY
        # 飞行模式
        ConnectionType.AIRPLANE_MODE
        # 无网络模式
        ConnectionType.NO_CONNECTION
        # 全部都打开
        ConnectionType.ALL_NETWORK_ON
    '''

    def getwebstate(self):
        """
        获取当前网络的状态
        """
        info = {0: "NO_CONNECTION（没网络）",

                1: "AIRPLANE_MODE（飞行模式）",

                2: "WIFI_ONLY（仅wifi）",

                4: "DATA_ONLY（仅数据）",

                6: "ALL_NETWORK_ON（所有网络都打开）"}

        state = self.driver.network_connection
        return info.get(state)

    def wifi(self):
        """
        仅wifi
        """
        # 设置 网络
        self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        print(self.getwebstate())

    def only(self):
        """
        仅数据
        """
        self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        print(self.getwebstate())

    def airplane_mode(self):
        """
        飞行模式
        """
        self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        print(self.getwebstate())

    def all_networe_on(self):
        """
        所有网络都打开
        """
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        print(self.getwebstate())