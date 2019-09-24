#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import requests
import urllib
from urllib import parse,request
import json
from  test_interfacecase.bussiness import sha1
import time

def get_generate_headers(data):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    time_now = time.time()
    #urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
    data_new = parse.urlencode(data)
    data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
    data_str = ''.join(data_list)
    sign_data = sha1.str_encrypt(data_str.encode("utf8"))
    sign_data = sign_data.lower()

    headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now), \
               "WL-SIGN": sign_data,"WL-TID" : "a50b0fff867a8ab8f252bb65f321e6bb"}

    return headers



