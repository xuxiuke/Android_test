#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_byphone(object):
    def __init__(self):
        pass


    def login_byphone(self):
        read_csv = Kernal_function('login/byphone')
        return read_csv.sso_post_answer()["resultCode"]

    def dispose(self):
        pass

        # # 读取csv文件数据
        # new = Read_file('demo_cloud.csv')
        # csv_dict = new.read_csv()
        # # 获取到的字符串格式数据转换成dict格式
        # interface = json.loads(csv_dict['login/byphone'], encoding='utf-8')
        # # 读取url的value
        # url = get_serveraddress.get_serveraddress()[0] + interface["url"]
        # # 读取url的data
        # data = interface["data"]
        # headers = generate_headers(data)
        # r = requests.post(url=url, json=data, headers=headers)  # 发送请求
        # # print(r.text)  # 获取响应报文
        # # print("接口:",interface["url"] ,"状态" ,"status_code:", r.status_code)
        # answer = json.loads(r.text, encoding='utf-8')
        # return answer["resultCode"]  # 获取resultCode

    # hello = Login_byphone()
# hello.login_byphone()








    # def test():
#     new = Read_file('demo_cloud.csv')
#     csv_list = new.read_csv()
#     for row in csv_list:
#         url = "https://testv2.wulian.cc:50090/sso/" + row['key']   # 测试的接口url
#         if row['method'] == 'post':
#             data = json.loads(row['value'], encoding='utf-8')
#             headers = generate_headers(data)
#             r = requests.post(url=url, json=data, headers=headers)  # 发送请求
#             print(r.text)  # 获取响应报文
#             print("接口:",row['key'] ,"状态" ,"status_code:", r.status_code)


