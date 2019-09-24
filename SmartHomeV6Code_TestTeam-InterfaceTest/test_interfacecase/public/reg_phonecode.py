#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Reg_phonecode(object):
    def __init__(self):
        pass

    def reg_phonecode(self):
        read_csv = Kernal_function('reg/phonecode')
        return read_csv.sso_get_answer()["resultCode"]  # 获取resultCode

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
# from  bussiness.get_headers import get_generate_headers
# from  bussiness.open_csv import Read_file
# from  bussiness import get_serveraddress
        # # # 读取csv文件数据
        # new = Read_file('demo_cloud.csv')
        # csv_dict = new.read_file()
        # #
        # #
        # # # 获取到的字符串格式数据转换成dict格式
        # interface = json.loads(csv_dict['reg/phonecode'], encoding='utf-8')
        # #读取url的value
        # url = get_serveraddress.get_serveraddress()[0] + interface["url"]
        # # # 读取url的data
        # data = interface["data"]
        # headers = get_generate_headers(data)
        # req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        # r = requests.get(url=req_url, headers=headers)  # 发送请求
        # # # print(r.text)  # 获取响应报文
        # # #print("接口:", interface["url"], "状态", "status_code:", r.status_code)
        # answer = json.loads(r.text, encoding='utf-8')
        # print(answer["resultCode"])






# reg_phonecode = Reg_phonecode()
# reg_phonecode.reg_phonecode()










