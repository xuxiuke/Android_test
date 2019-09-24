#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import json
import csv
import urllib
from urllib import parse,request
# from  bussiness.open_csv import Read_file
# from  bussiness import get_serveraddress
# from  bussiness.sso_get_headers import get_generate_headers
# from  bussiness.sso_post_headers import post_generate_headers
# from  bussiness import sha1
import requests

from test_interfacecase.bussiness.sso_post_headers import post_generate_headers


class Reg_bythird(object):
    def __init__(self):   #,status_code = 200
        pass

    def reg_bythird(self):
        url = "https://testv2.wulian.cc:50090/sso/reg/bythird"
        for i in range(3):
            i = i + 1
            j = 0
            if i == 1:
                data = {
                    "thirdType": i,
                    "openId": "ovQgr0upGkMQ1ztcFivYTpwBY3LA",
                    "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
                    "avatar": "http:\/\/wx.qlogo.cn\/mmopen\/5RCxkL3Un85WDJ6KIez7arY9QyayoFEhkEBXzZia2EZwJlUgaWp\
                    J44FhVhtkQUyFmcicooiaLrUwIzkuxicfhWTtlMvZMBn5tCsv\/0",
                    "nick": "人来人往",
                    "phone": "13776627090",
                    "phoneCountryCode":"86",
                    "email":"***",
                    "password":"e10adc3949ba59abbe56e057f20f883e"
                    }  # 接口数据

                headers = post_generate_headers(data)
                #print(headers)
                r = requests.post(url=url, json=data, headers=headers)  # 发送请求
                #print(r.text)
                postanswer = json.loads(r.text, encoding='utf-8')
                #print(postanswer)
                j = j + int(postanswer["resultCode"])
                #print(j)

#####缺少删除账号的接口，导致只能注册一个账号


            elif i == 2:
                data = {
                    "thirdType": i,
                    "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
                    "openId": "8005329582F41D11944FA953FB526A13",
                    "avatar": "http:\/\/q.qlogo.cn\/qqapp\/1106062262\/8005329582F41D11944FA953FB526A13\/100",
                    "nick": "人来人往",
                    "phone": "13776627095",
                    "phoneCountryCode": "86",
                    "email": "***",
                    "password": "e10adc3949ba59abbe56e057f20f883e"
                }  # 接口数据

                headers = post_generate_headers(data)
                r = requests.post(url=url, json=data, headers=headers)  # 发送请求
                postanswer = json.loads(r.text, encoding='utf-8')
                j = j + int(postanswer["resultCode"])

            elif i == 3:
                data = {
                    "thirdType": i,
                    "openId": "1820499241",
                    "avatar": "http:\/\/tvax2.sinaimg.cn\/crop.0.25.1242.1242.50\/6c829d29ly8ff1olwh2lhj20yi0zxwo3.jpg",
                    "nick": "Flush0702",
                    "phone": "13776627095",
                    "phoneCountryCode":"86",
                    "email":"***",
                    "password":"e10adc3949ba59abbe56e057f20f883e"
                }  # 接口数据

                headers = post_generate_headers(data)
                r = requests.post(url=url, json=data, headers=headers)  # 发送请求
                postanswer = json.loads(r.text, encoding='utf-8')
                j = j + int(postanswer["resultCode"])
            print(str(j))
            return str(j)


login = Reg_bythird()
login.reg_bythird()









