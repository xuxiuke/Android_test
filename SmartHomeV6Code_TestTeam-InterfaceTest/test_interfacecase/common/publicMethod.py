# get请求
import json
import random
from urllib import parse
import requests
from test_interfacecase.common import header
from test_interfacecase.common.connectInterface import connectInterface
# 公共方法类


#get请求
def getRequest(url, data):
    getReturn=connectInterface().connect()
    if "token" in data:
        data["token"]=getReturn["data"]["token"]
    url = url + "?" + parse.urlencode(data)
    print(url)
    hd = header.getHeader(data)
    r = requests.get(url=url, headers=hd)
    return json.loads(r.text, encoding="utf-8")


# post请求
def postRequest(url, data):
    hd = header.postHeader(data)
    r = requests.post(url=url, json=data, headers=hd)
    t=json.loads(r.text, encoding="utf-8")
    return t

#随机生成四位数
def randomMethod():
    ra=""
    for i in range(4):
        ra += str(random.randint(0, 9))
    return ra



data = {
        "thirdType": 2,
        "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
        "openId": "7736BA7611D9EEBCBAA89DC3785E6247",
        "phone": "18168020465",
        "phoneCountryCode": "86",
        "email": "***",
        "password": "e9ea90857363708afc42938a00719e76"
    }
url="https://iotsh.wuliancloud.com:443/sso/reg/bythird"
# data["openId"]="8005329582F41D11944FA953FB52"+randomMethod()
# p=postRequest(url,data)
# print(p)









# data1={"token":"token"}
# url1="https://iotsh.wuliancloud.com:443/sso/token/mqtt"
# g=getRequest(url1,data1)
# print(g)
