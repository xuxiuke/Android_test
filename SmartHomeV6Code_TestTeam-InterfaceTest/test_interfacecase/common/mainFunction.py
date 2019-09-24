# coding=utf-8

import json
from urllib import parse
import requests
from test_interfacecase.common import header
from test_interfacecase.common.connectInterface import connectInterface
from test_interfacecase.common.publicMethod import randomMethod, postRequest
from test_interfacecase.common.readFile import readFile
from test_interfacecase.common.serverAddress import serverAddress

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

adressIndex = 1  # 切换环境，0：正式环境 1：测试环境 3：美西环境


class mainFunction(object):
    def __init__(self, key):
        self.key = key
        self.dict = readFile("demo_cloud.csv").readfile()

    def ssoGetAnswer(self):
        # 反序列化，将字符串转化为python格式
        interface = json.loads(self.dict[self.key], encoding="utf-8")
        url = serverAddress().getAddress()[adressIndex] + interface["url"]
        data = interface["data"]
        getReturn = connectInterface().connect()
        print(getReturn)
        if "token" in data:
            data["token"] = getReturn["data"]["token"]
        getUrl = url + "?" + parse.urlencode(data, encoding="utf-8")
        print("getUrl:" + getUrl)
        hd = header.getHeader(data)
        r = requests.get(url=getUrl, headers=hd)
        return json.loads(r.text, encoding="utf-8")

    def ssoPostAnswer(self):
        # 反序列化，将字符串转化为python格式
        interface = json.loads(self.dict[self.key], encoding="utf-8")
        url = serverAddress().getAddress()[adressIndex] + interface["url"]
        data = interface["data"]
        getReturn = connectInterface().connect()
        print(getReturn)
        if "token" in data:
            data["token"] = getReturn["data"]["token"]
        hd = header.postHeader(data)
        r = requests.post(url=url, json=data, headers=hd)
        return json.loads(r.text, encoding="utf-8")

    # 三方账号登录时绑定的手机或邮箱没有注册过账号，利用该手机或邮箱注册新的账号
    def regBythirdAnswer(self):
        # 反序列化，将字符串转化为python格式
        interface = json.loads(self.dict[self.key], encoding="utf-8")
        url = serverAddress().getAddress()[adressIndex] + interface["url"]
        data = interface["data"]
        data["openId"] = "8005329582F41D11944FA953FB52" + randomMethod()
        return postRequest(url, data)

    # api接口的签名规则与sso一致
    def apiGetAnswer(self):
        # 反序列化，将字符串转化为python格式
        interface = json.loads(self.dict[self.key], encoding="utf-8")
        url = serverAddress().getAddress()[adressIndex] + interface["url"]
        data = interface["data"]
        getReturn = connectInterface().connect()
        print(getReturn)
        if "token" in data:
            data["token"] = getReturn["data"]["token"]
        if "uId" in data:
            data["uId"] = getReturn["data"]['uId']
        getUrl = url + "?" + parse.urlencode(data, encoding="utf-8")
        getUrl = parse.unquote(getUrl)  # 解码  处理特殊字符
        print("getUrl:" + getUrl)
        hd = header.apiGetHeader(data, getReturn["data"]["token"])
        r = requests.get(url=getUrl, headers=hd)
        print(r.text)
        return json.loads(r.text, encoding="utf-8")

    # api接口的签名规则与sso一致
    def apiPostAnswer(self):
        # 反序列化，将字符串转化为python格式
        interface = json.loads(self.dict[self.key], encoding="utf-8")
        url = serverAddress().getAddress()[adressIndex] + interface["url"]
        data = interface["data"]
        getReturn = connectInterface().connect()
        print(getReturn)
        if "token" in data:
            data["token"] = getReturn["data"]["token"]
        if "uId" in data:
            data["uId"] = getReturn["data"]['uId']
        hd = header.apiPostHeader(data, getReturn["data"]["token"])
        r = requests.post(url=url, json=data, headers=hd)
        return json.loads(r.text, encoding="utf-8")
