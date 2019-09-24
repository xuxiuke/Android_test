#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import requests
import json
from mqtt_test.mqtt_bussiness import sha1
from mqtt_test.mqtt_bussiness import sso_post_headers
import time


def iot_get_return():
    url = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url

    data = {
    "phone": "13675124538",
    "phoneCountryCode": 86,
    "password": "e9ea90857363708afc42938a00719e76",
    "terminalId":"a50b0fff867a8ab8f252bb65f321e6bb"
        }  # 接口数据

    headers = sso_post_headers.post_generate_headers(data)
    r = requests.post(url=url,  json = data, headers=headers)  # 发送请求
    return_data = json.loads(r.text)
    #print (return_data)
    return return_data


