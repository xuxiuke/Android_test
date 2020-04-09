#coding=utf-8

"""
作者: Duke
文件名: step.py
创建时间: 2020/04/08-08:57
"""

from Search_baidu import base
import time


class Login(base.Action):

    # 1、搜索流程：南京物联
    def search(self):
        self.find_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextSwitcher[1]/android.widget.TextView[1]').click()
        self.find_xpath("//android.widget.EditText[@resource-id='com.baidu.searchbox:id/SearchTextInput']").send_keys('南京物联')
        self.find_id('com.baidu.searchbox:id/float_search_or_cancel').click()  # 百度一下
        time.sleep(7)
        self.find_xpath('//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.TabHost[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.TextSwitcher[1]/android.widget.TextView[1]').click()
        time.sleep(5)
        self.airplane_mode()  # 设置飞行模式
        time.sleep(5)
        while True:
            if self.getwebstate() != 4:
                self.only()  # 设置为数据模式
                time.sleep(2)
                return True