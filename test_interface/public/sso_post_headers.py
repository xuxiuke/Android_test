# coding=utf-8

"""
作者: Duke
文件名: sso_post_headers.py
创建时间: 2019/09/12-09:37
"""

import json
from public import sha1
import time


def post_generate_headers(data):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    time_now = time.time()

    data_new = json.dumps(data)  # 将字典形式的数据转化为字符串
    data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
    data_str = ''.join(data_list)
    sign_data = sha1.str_encrypt(data_str.encode("utf8"))
    sign_data = sign_data.lower()
    headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
               "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
    return headers
