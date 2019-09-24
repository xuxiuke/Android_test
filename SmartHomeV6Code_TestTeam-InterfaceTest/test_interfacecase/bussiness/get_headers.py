# coding=utf-8

from urllib import parse
from test_interfacecase.bussiness import sha1
import time
from collections import OrderedDict


class Get_headers(object):
    def __init__(self, data):
        self.data = data

    def api_get_generate_headers(self, token):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        time_now = int(round(time_now * 1000))
        # 生成有序的字典
        result_data = OrderedDict()
        get_data = sorted(self.data)
        # print(get_data)
        for k in get_data:
            result_data[k] = self.data[k]
        # print(result_data)
        data_new = parse.urlencode(result_data)
        data_new = parse.unquote(data_new)  # 解码,处理特殊字符

        if not data_new:
            data_list = [partnerId, '&', data_new, partnerkey, '&', str(time_now)]
        else:
            data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]

        data_str = ''.join(data_list)
        # print(data_str)  #加密前的字符串
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        # print(sign_data)  #签名后的数据
        # token = get_token.test_get_token()
        # get_return = iot_get_return()
        # token = get_return["data"]['token']
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb", "WL-TOKEN": token}
        return headers

    def sso_get_generate_headers(self):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        time_now = int(round(time_now * 1000))
        # 生成有序的字典
        result_data = OrderedDict()
        get_data = sorted(self.data)
        # print(get_data)
        for k in get_data:
            result_data[k] = self.data[k]
        # print(result_data)
        data_new = parse.urlencode(result_data)
        # print(data_new)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
        return headers

    def ent_get_generate_headers(self):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        time_now = time.time()
        time_now = int(round(time_now * 1000))
        # 生成有序的字典
        result_data = OrderedDict()
        get_data = sorted(self.data)
        # print(get_data)
        for k in get_data:
            result_data[k] = self.data[k]
        # print(result_data)
        data_new = parse.urlencode(result_data)
        # print(data_new)
        data_list = [partnerId, '&', data_new, '&', partnerkey, '&', str(time_now)]
        data_str = ''.join(data_list)
        sign_data = sha1.str_encrypt(data_str.encode("utf8"))
        sign_data = sign_data.lower()
        headers = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(time_now),
                   "WL-SIGN": sign_data, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
        return headers
