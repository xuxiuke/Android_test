import json
import time
from collections import OrderedDict
from urllib import parse

from test_interfacecase.bussiness import sha1

# 每个app会分配一个partnerId和partnerKey
# 签名规则：
# partnerId + "&" + 参数部分 + "&" + partnerKey + "&" + 当前时间戳(毫秒)
# 上述字符串进行sha1加密然后转换成小写字符串, 就是本次请求的签名
# 对于GET请求
# 参数部分为：所有参数按照参数名升序排序，通过"&"拼接起来
# 对于POST请求
# 参数部分为：request的body


def getHeader(data):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    t = time.time()
    nowtime = int(round(t * 1000))  # 获取毫秒级时间戳  # 获取get的header
    # 字典类型的data升序排序
    ordict=OrderedDict()
    da=sorted(data)
    for i in da:
        ordict[i]=data[i]
    # urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
    dataNow = parse.urlencode(ordict,encoding="utf-8")
    sign = partnerId + "&" + dataNow + "&" + partnerkey + "&" + str(nowtime)
    # 或者这么写
    # data_list = [partnerId, '&', dataNow, '&', partnerkey, '&', str(nowtime)]
    # sign = ''.join(data_list)
    sign = sha1.str_encrypt(sign.encode("utf-8")).lower()
    header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(nowtime),
              "WL-SIGN": sign, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
    return header


# 获取postheader
def postHeader(data):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    t = time.time()
    nowtime = int(round(t * 1000))  # 获取毫秒级时间戳  # 获取get的header
    print(nowtime)
    # 将data序列化为json字符串
    dataNow = json.dumps(data)
    sign = partnerId + "&" + dataNow + "&" + partnerkey + "&" + str(nowtime)
    print(sign)
    signed = sha1.str_encrypt(sign.encode("utf8")).lower()
    print(signed)
    header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(nowtime),
              "WL-SIGN": signed, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
    return header

def apiPostHeader(data,token):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    t = time.time()
    nowtime = int(round(t * 1000))  # 获取毫秒级时间戳  # 获取get的header
    # 将data序列化为json字符串
    dataNow = json.dumps(data)
    sign = partnerId + "&" + dataNow + "&" + partnerkey + "&" + str(nowtime)
    signed = sha1.str_encrypt(sign.encode("utf8")).lower()
    # print(signed)
    header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(nowtime),
              "WL-SIGN": signed, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb","WL-TOKEN": token}
    return header

def apiGetHeader(data,token):
    partnerId = "wulian_app"
    partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
    t = time.time()
    nowtime = int(round(t * 1000))  # 获取毫秒级时间戳  # 获取get的header
    # 字典类型的data升序排序
    ordict=OrderedDict()
    da=sorted(data)
    for i in da:
        ordict[i]=data[i]
    # urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，返回的是a=1&b=2这样的字符串
    dataNow = parse.urlencode(ordict,encoding="utf-8")
    dataNow=parse.unquote(dataNow) #处理字符中的特殊字符，有@、#、￥之类的
    sign = partnerId + "&" + dataNow + "&" + partnerkey + "&" + str(nowtime)
    sign = sha1.str_encrypt(sign.encode("utf-8")).lower()
    header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": str(nowtime),
              "WL-SIGN": sign, "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb","WL-TOKEN": token}
    return header





