#coding=utf-8

"""
作者: Duke
文件名: open_baidu.py
创建时间: 2020/04/08-08:53
"""

from Search_baidu import step
import time
from appium import webdriver


class Open_baidu(step.Login):

    def open(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'TPE9X18516W00552',
            'noReset': True,  # 不用每次清除数据
            'resetKeyboard': True,
            "unicodeKeyboard": True,
            'appPackage': 'com.baidu.searchbox',
            'appActivity': '.MainActivity',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('打开APP成功')
        time.sleep(10)
        # self.driver.implicitly_wait(30)  # 智能等待30s

    def get_driver(self):
        driver = self.driver
        return driver

    def after(self):
        time.sleep(5)
        self.driver.quit()