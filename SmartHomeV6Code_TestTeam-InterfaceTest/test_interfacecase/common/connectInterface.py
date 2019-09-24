import json

import requests

from test_interfacecase.bussiness import sso_post_headers
from test_interfacecase.common import header

#账号密码尝试连接
class connectInterface(object):

    @staticmethod
    def connect():
        url = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url
        # data = {
        #     "phone": "18168020465",
        #     "phoneCountryCode": 86,
        #     "password": "e9ea90857363708afc42938a00719e76",
        #     "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
        # }  # 接口数据
        data = {
            "phone": "15951644332",
            "phoneCountryCode": 86,
            "password": "bc9b5718afdffe85fb13555347969ff5",
            "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
        }  # 接口数据
        hd=header.postHeader(data)
        print(data)
        r = requests.post(url=url,json=data,headers=hd)
        # dat={"token": "9de864beb83e69b020eec15b0d037163"}
        # hd=header.getHeader(dat)
        # r=requests.get(url="https://iot.wuliancloud.com:443/sso/token/mqtt",headers=hd)
        getReturn=json.loads(r.text,encoding="utf-8")
        return getReturn




# c=connectInterface()
# print(c.connect())