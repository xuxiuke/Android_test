#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import requests
import json
from  test_interfacecase.bussiness import sha1
from  test_interfacecase.bussiness import sso_post_headers
import time


def test_get_token():
    url = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url


    data = {
    "phone": "13675124538",
    "phoneCountryCode": 86,
    "password": "e9ea90857363708afc42938a00719e76",
    "terminalId":"***"
        }  # 接口数据

    headers = sso_post_headers.post_generate_headers(data)
    r = requests.post(url=url,  json = data, headers=headers)  # 发送请求
    #print(r.text)
    hjson = json.loads(r.text)
    token = hjson['data']['token']
    #print (hjson)
    return token

#test_get_token()




