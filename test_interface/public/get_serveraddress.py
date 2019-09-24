#coding=utf-8

"""
作者: Duke
文件名: get_serveraddress.py
创建时间: 2019/09/12-09:04
"""

def get_serveraddress():
    serveraddress = []
    serveraddress1 = "https://iotsh.wuliancloud.com:443/"
    serveraddress2 = "https://testv6.wulian.cc/"
    serveraddress3 = "https://testv2.wulian.cc:50090/"
    serveraddress4 = "https://iot.wuliancloud.com/"

    for i in (serveraddress1, serveraddress2, serveraddress3, serveraddress4):
        serveraddress.append(i)
    return serveraddress
