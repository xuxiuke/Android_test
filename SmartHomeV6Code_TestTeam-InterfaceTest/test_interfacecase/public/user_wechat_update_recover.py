#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import requests
import json
import csv
from  test_interfacecase.bussiness import sha1
import time
from urllib import parse,request
from  test_interfacecase.bussiness import get_serveraddress
from test_interfacecase.bussiness.read_csv import Read_csv
from  test_interfacecase.bussiness.kernal_function import Kernal_function
from  test_interfacecase.bussiness.post_headers import Post_headers
from  test_interfacecase.bussiness.sso_post_headers import post_generate_headers
from  test_interfacecase.bussiness import global_value


class User_wechat_update_recover(object):
    def __init__(self):
        pass

    def user_wechat_update_recover(self):
        url_token = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url
        data = {
            "phone": "18168020465",
            "phoneCountryCode": "86",
            "password": "eab7c169c851f1462a140448a299d8a6",
            "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
        }  # 接口数据
        headers = post_generate_headers(data)
        r = requests.post(url=url_token, json=data, headers=headers)  # 发送请求
        get_return = json.loads(r.text)
        global_value.set_get_return_value(get_return)
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict["user/wechat/update_recover"], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[0] + interface["url"]
        # 读取url的data
        data = interface["data"]
        # 判断uId 和token 字符串
        if "uId" in data:
            data["uId"] = get_return["data"]['uId']
        # 读取url的data
        if "token" in data:
            data["token"] = get_return["data"]['token']
        get_headers = Post_headers(data)
        headers = get_headers.api_post_generate_headers(get_return["data"]['token'])
        r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        postanswer = json.loads(r.text, encoding='utf-8')
        return postanswer["resultCode"]


    def dispose(self):
        pass