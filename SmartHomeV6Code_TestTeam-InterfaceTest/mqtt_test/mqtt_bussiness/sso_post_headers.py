#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import requests
import json
from  mqtt_test.mqtt_bussiness import sha1
import time

def post_generate_headers(data):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    time_now = time.time()

    data_new = json.dumps(data)
    data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
    data_str = ''.join(data_list)
    # data_str = partnerId + '&' + data_new + '&' + partnerkey + '&'+ str(time.time())
    #print(data_str)
    sign_data = sha1.str_encrypt(data_str.encode("utf8"))
    sign_data = sign_data.lower()
    #print(sign_data)
    headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now), \
               "WL-SIGN": sign_data,"WL-TID" : "a50b0fff867a8ab8f252bb65f321e6bb"}
    return headers
