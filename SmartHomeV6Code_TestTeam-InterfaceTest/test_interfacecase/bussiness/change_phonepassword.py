#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.sso_post_headers import post_generate_headers
import requests
import json
import csv
from  test_interfacecase.bussiness import sha1
import time

class Change_phone_password(object):
    def __init__(self):
        pass
    def change_phone_password(self):
        url_token = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url
        data = {
            "phone": "18168020465",
            "phoneCountryCode": "86",
            "password": "210b48b542659fb951a80a15c5997513",
            "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
        }  # 接口数据
        headers = post_generate_headers(data)
        r = requests.post(url=url_token, json=data, headers=headers)  # 发送请求
        hjson = json.loads(r.text)
        token = hjson['data']['token']

        url = "https://iot.wuliancloud.com:443/api/user/updatepass"  # 测试的接口url
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()

        data_recover = {
            "password": "210b48b542659fb951a80a15c5997513",
            "newpassword": "eab7c169c851f1462a140448a299d8a6"
        }   # 接口数据


        data_new = json.dumps(data_recover)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        #print(data_str)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now), \
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb", "WL-TOKEN": token}
        #print (headers)

        r = requests.post(url=url, json=data_recover, headers=headers)  # 发送请求
        print(r.text)
        return r

# c=Change_phone_password()
# c.change_phone_password()