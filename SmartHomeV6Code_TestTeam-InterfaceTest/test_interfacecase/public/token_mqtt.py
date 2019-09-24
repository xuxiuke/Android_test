#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Token_mqtt(object):
    def __init__(self):
        pass


    def token_mqtt(self):
        read_csv = Kernal_function('token/mqtt')
        return read_csv.sso_get_answer()["resultCode"]

    def dispose(self):
        pass







# import requests
# import json
# from  bussiness import sha1
# import time
# import csv
# import urllib
# from urllib import parse,request
# from  bussiness import get_token
# from  bussiness.sso_get_headers import get_generate_headers
# from  bussiness.open_csv import Read_file
# from  bussiness import get_serveraddress

# class Token_mqtt(object):
#     def __init__(self):
#         pass
#
#     def token_mqtt(self):
#         url = "https://testv2.wulian.cc:50090/sso/token/mqtt"  # 测试的接口url
#         token = get_token.test_get_token()  # 接口数据
#         #print (token)
#         data = {
#             "token": token
#         }
#         headers = get_generate_headers(data)
#         req_url = url + '?' + parse.urlencode(data)  # 构建get请求
#         r = requests.get(url=req_url, headers=headers)  # 发送请求
#         answer = json.loads(r.text, encoding='utf-8')
#         return answer["resultCode"]  # 获取resultCode
#
#
#
#     def dispose(self):
#         pass


# new = Token_mqtt()
# new.token_mqtt()





