# coding=utf-8

"""
Created on 2018年8月17日

@author: Duke    打开APP,登陆APP
"""

from step import a01_login
import time
from appium import webdriver


class Open_app(a01_login.Login):

    def open(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'TPE9X18516W00552',
            # 'deviceName': 'R8V5T15629001602',
            'noReset': True,  # 不用每次清除数据
            'resetKeyboard': True,
            "unicodeKeyboard": True,
            # 'app': 'D:\\test\\appium_test\APP\SmartHomev6.2.9.apk',
            'appPackage': 'com.wlinkapp',
            'appActivity': 'com.wlinkapp.MainActivity',
            # 'appPackage': 'cc.wulian.smarthomev6',
            # 'appActivity': 'cc.wulian.smarthomev6.main.welcome.SplashActivity',
            'automationName': 'Uiautomator2'  # 定位toast元素
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('打开APP成功')
        # self.swipLeft(1000)
        # time.sleep(1)
        # self.swipLeft(1000)
        # time.sleep(1)
        # self.swipLeft(1000)
        # time.sleep(1)
        # self.find_id('cc.wulian.smarthomev6:id/guide_tv').click()
        time.sleep(10)
        # self.driver.implicitly_wait(30)  # 智能等待30s

    def get_driver(self):
        driver = self.driver
        return driver

    def after(self):
        time.sleep(5)
        self.driver.quit()
