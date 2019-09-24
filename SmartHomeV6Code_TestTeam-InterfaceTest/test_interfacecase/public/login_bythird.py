#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function


class Login_bythird(object):
    def __init__(self):
        pass

    def login_bythird(self):
        read_csv = Kernal_function('login/bythird')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass




    # def login_bythird(self):
    #     url = "https://testv2.wulian.cc:50090/sso/login/bythird"
    #     for i in range(3):
    #         i = i + 1
    #         j = 0
    #         if i == 1:
    #             data = {
    #                 "thirdType": i,
    #                 "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
    #                 "openId": "ovQgr0upGkMQ1ztcFivYTpwBY3LA",
    #                 "avatar": "http:\/\/wx.qlogo.cn\/mmopen\/5RCxkL3Un85WDJ6KIez7arY9QyayoFEhkEBXzZia2EZwJlUgaWp\
    #                 J44FhVhtkQUyFmcicooiaLrUwIzkuxicfhWTtlMvZMBn5tCsv\/0",
    #                 "nick": "人来人往",
    #                 "gender": 0
    #             }  # 接口数据
    #
    #             headers = post_generate_headers(data)
    #             r = requests.post(url=url, json=data, headers=headers)  # 发送请求
    #             postanswer = json.loads(r.text, encoding='utf-8')
    #             j = j + int(postanswer["resultCode"])
    #
    #         elif i == 2:
    #             data = {
    #                 "thirdType": i,
    #                 "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
    #                 "openId": "8005329582F41D11944FA953FB526A13",
    #                 "avatar": "http:\/\/q.qlogo.cn\/qqapp\/1106062262\/8005329582F41D11944FA953FB526A13\/100",
    #                 "nick": "人来人往",
    #                 "gender": 0
    #             }  # 接口数据
    #
    #             headers = post_generate_headers(data)
    #             r = requests.post(url=url, json=data, headers=headers)  # 发送请求
    #             postanswer = json.loads(r.text, encoding='utf-8')
    #             j = j + int(postanswer["resultCode"])
    #
    #         elif i == 3:
    #             data = {
    #                 "thirdType": i,
    #                 "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
    #                 "openId": "1820499241",
    #                 "avatar": "http:\/\/tvax2.sinaimg.cn\/crop.0.25.1242.1242.50\/6c829d29ly8ff1olwh2lhj20yi0zxwo3.jpg",
    #                 "nick": "Flush0702",
    #                 "gender": 0
    #             }  # 接口数据
    #
    #             headers = post_generate_headers(data)
    #             r = requests.post(url=url, json=data, headers=headers)  # 发送请求
    #             postanswer = json.loads(r.text, encoding='utf-8')
    #             j = j + int(postanswer["resultCode"])
    #
    #         return str(j)
    #



# login = Login_bythird()
# login.login_bythird()









