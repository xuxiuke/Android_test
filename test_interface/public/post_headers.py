# coding=utf-8

"""
作者: Duke
文件名: post_headers.py
创建时间: 2019/09/12-09:11
"""

import base64
import json
from public import sha1
import time


class Post_headers(object):

    def __init__(self, data):
        self.data = data

    def sso_post_generate_headers(self):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        data_new = json.dumps(self.data)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
        return headers

    def api_post_generate_headers(self, token):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        data_new = json.dumps(self.data)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb", "WL-TOKEN": token}
        return headers

    @staticmethod
    def api_icampost_generate_headers():
        user = "cmic"
        password = "d7a3ae6f06171748d82314915bc73820"
        Authorization = base64.b64encode((user + ":" + password).encode("utf-8"))
        Authorization = Authorization.decode()
        headers = {"Content-Type": "application/json", "Authorization": Authorization}
        return headers

    def ent_post_generate_headers(self):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        data_new = json.dumps(self.data)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
        return headers
