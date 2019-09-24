# coding=utf-8

import json
import time
import requests
from urllib import parse
from test_interfacecase.bussiness.read_csv import Read_csv
from test_interfacecase.bussiness import get_serveraddress
from test_interfacecase.bussiness.get_headers import Get_headers
from test_interfacecase.bussiness.post_headers import Post_headers
from test_interfacecase.bussiness.cloud_iot.iot_generate_nonce import iot_generate_nonce
from test_interfacecase.bussiness.cloud_iot.iot_get_msgContent_sianature import Iot_aes
from test_interfacecase.bussiness.cloud_iot.iot_get_return import iot_get_return
from test_interfacecase.bussiness.cloud_iot.iot_encry_decry import Iot_encry_decry
from test_interfacecase.bussiness.cloud_iot.iot_base64 import Base64
from test_interfacecase.bussiness import global_value

"""
每个app会分配一个partnerId和partnerKey
签名规则：
partnerId + "&" + 参数部分 + "&" + partnerKey + "&" + 当前时间戳(毫秒)
上述字符串进行sha1加密然后转换成小写字符串, 就是本次请求的签名
对于GET请求
参数部分为：所有参数按照参数名升序排序，通过
"&"
拼接起来
对于POST请求
参数部分为：request的body
"""

adressIndex = 0  # 切换环境，0：正式环境 1：测试环境 3：美西环境


class Kernal_function(object):

    def __init__(self, key):
        self.key = key

    def sso_get_answer(self):
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        if global_value.get_execute_value() == "1":
            get_return = iot_get_return()
            # 更改参数的data
            if "token" in data:
                data["token"] = get_return["data"]['token']
        get_headers = Get_headers(data)
        headers = get_headers.sso_get_generate_headers()
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        r = requests.get(url=req_url, headers=headers)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        return getanswer

    def api_get_answer(self):
        get_return = iot_get_return()
        print(get_return)
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        # 判断uId 和token 字符串
        if "uId" in data:
            data["uId"] = get_return["data"]['uId']
        # 读取url的data
        if "token" in data:
            data["token"] = get_return["data"]['token']
        get_headers = Get_headers(data)
        headers = get_headers.api_get_generate_headers(get_return["data"]['token'])
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        req_url = parse.unquote(req_url)  # 解码  处理特殊字符
        r = requests.get(url=req_url, headers=headers)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        print(getanswer)
        return getanswer

    def sso_post_answer(self):
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        if global_value.get_execute_value() == "1":
            get_return = global_value.get_get_return_value()
            # 更改参数的data
            if "token" in data:
                data["token"] = get_return["data"]['token']
        get_headers = Post_headers(data)
        headers = get_headers.sso_post_generate_headers()
        r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        print(r)
        postanswer = json.loads(r.text, encoding='utf-8')
        return postanswer

    def api_post_answer(self):
        get_return = iot_get_return()
        print(get_return)
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        # 判断uId 和token 字符串
        if "uId" in data:
            data["uId"] = get_return["data"]['uId']
        # 读取url的data
        if "token" in data:
            data["token"] = get_return["data"]['token']
        # if "unionId" in data:
        #     if data["unionId"]=="ovQgr0rNtJ03yV3bN9xlTjzQUM0":
        #         data["unionId"]="ovQgr0rNtJ03yV3bN9xlTjz"+publicMethod.randomMethod()
        get_headers = Post_headers(data)
        headers = get_headers.api_post_generate_headers(get_return["data"]['token'])
        r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        postanswer = json.loads(r.text, encoding='utf-8')
        return postanswer

    def iot_get_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        secretKey = get_return["data"]['secretKey']  # 每个接口必须要传AESkey
        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        r = requests.get(url=req_url)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        msgContent = getanswer['msgContent']
        # 解密msgContent
        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        return_data = Iot_encry_decry(msgContent_base64, secretKey, secretuId)
        return_data = return_data.decry()
        return return_data

    def iot_post_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        secretKey = get_return["data"]['secretKey']  # 每个接口必须要传AESkey
        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        generate_nonce = iot_generate_nonce()  # 产生随机数
        timestamp = time.time()
        timestamp = str(int(round(timestamp * 1000)))
        data = json.dumps(data)  # 字符串数据
        iot_aes = Iot_aes(data, secretKey, generate_nonce, timestamp, secretuId)
        msgContent = iot_aes.get_msgContent()
        signature = iot_aes.get_signature()
        message = {"signature": signature, "nonce": generate_nonce, "timestamp": timestamp, "msgContent": msgContent}
        r = requests.post(url=url, json=message)  # 发送请求
        postanswer = json.loads(r.text, encoding='utf-8')
        print(postanswer)
        msgContent = postanswer['msgContent']
        # 解密msgContent
        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        return_data = Iot_encry_decry(msgContent_base64, secretKey, secretuId)
        return_data = return_data.decry()
        return return_data

    def iot_delete_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        secretKey = get_return["data"]['secretKey']  # 每个接口必须要传AESkey
        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        r = requests.delete(url=req_url)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        msgContent = getanswer['msgContent']
        # 解密msgContent
        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        return_data = Iot_encry_decry(msgContent_base64, secretKey, secretuId)
        return_data = return_data.decry()
        return return_data

    def iot_icampost_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        get_headers = Post_headers(data)
        headers = get_headers.api_icampost_generate_headers()
        r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        postanswer = json.loads(r.text, encoding='utf-8')
        return postanswer

    def iot_put_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        secretKey = get_return["data"]['secretKey']  # 每个接口必须要传AESkey
        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        generate_nonce = iot_generate_nonce()  # 产生随机数
        timestamp = time.time()
        timestamp = str(int(round(timestamp * 1000)))
        data = json.dumps(data)  # 字符串数据
        iot_aes = Iot_aes(data, secretKey, generate_nonce, timestamp, secretuId)
        msgContent = iot_aes.get_msgContent()
        signature = iot_aes.get_signature()
        message = {"signature": signature, "nonce": generate_nonce, "timestamp": timestamp, "msgContent": msgContent}
        r = requests.put(url=url, json=message)  # 发送请求
        postanswer = json.loads(r.text, encoding='utf-8')
        msgContent = postanswer['msgContent']
        # 解密msgContent
        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        return_data = Iot_encry_decry(msgContent_base64, secretKey, secretuId)
        return_data = return_data.decry()
        return return_data

    def iot_icamget_answer(self):
        get_return = iot_get_return()
        csv_dict = Read_csv().read_csv()
        secretKey = get_return["data"]['secretKey']  # 每个接口必须要传AESkey
        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 判断uId 和token 字符串
        if "uId" in url:
            url = url.replace("uId", get_return["data"]['uId'])
        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        r = requests.get(url=req_url)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        return getanswer

    # ent post接口
    def entPostAnswer(self):
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        if global_value.get_execute_value() == "1":
            get_return = global_value.get_get_return_value()
            # 更改参数的data
            if "token" in data:
                data["token"] = get_return["data"]['token']
        get_headers = Post_headers(data)
        headers = get_headers.ent_post_generate_headers()
        r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        print(r)
        postanswer = json.loads(r.text, encoding='utf-8')
        return postanswer

    # ent get接口
    def entGetAnswer(self):
        csv_dict = Read_csv().read_csv()
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        # 读取url的value
        url = get_serveraddress.get_serveraddress()[adressIndex] + interface["url"]
        # 读取url的data
        data = interface["data"]
        if global_value.get_execute_value() == "1":
            get_return = iot_get_return()
            # 更改参数的data
            if "token" in data:
                data["token"] = get_return["data"]['token']
        get_headers = Get_headers(data)
        headers = get_headers.ent_get_generate_headers()
        req_url = url + '?' + parse.urlencode(data)  # 构建get请求
        r = requests.get(url=req_url, headers=headers)  # 发送请求
        getanswer = json.loads(r.text, encoding='utf-8')
        print(getanswer)
        return getanswer
