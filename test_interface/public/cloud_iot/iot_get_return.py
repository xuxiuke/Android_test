# coding=utf-8

"""
作者: Duke
文件名: iot_get_return.py
创建时间: 2019/09/12-09:36
"""

import requests
import json
from public import sso_post_headers
from public import global_value


def iot_get_return():
    url = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url

    data = {
        "phone": "18168020465",
        "phoneCountryCode": 86,
        "password": "eab7c169c851f1462a140448a299d8a6",
        "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
    }  # 接口数据

    headers = sso_post_headers.post_generate_headers(data)
    r = requests.post(url=url, json=data, headers=headers)  # 发送请求
    get_return = json.loads(r.text)
    global_value.set_get_return_value(get_return)
    return get_return
