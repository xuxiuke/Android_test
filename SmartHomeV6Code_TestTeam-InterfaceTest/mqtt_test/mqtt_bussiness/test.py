#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from test_interfacecase.bussiness.cloud_iot.iot_base64 import Base64
import base64
from Crypto.Cipher import AES
import json
import demjson



class Iot_encry_decry(object):
    def __init__(self,msg,AESkey):
        self.msg = msg
        self.AESkey = AESkey
        self.mode = AES.MODE_ECB
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def decry(self):
        # 直接传获取到的消息

        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        AESkey = self.AESkey + "=="  # 首先字符串拼接==
        AESkey = AESkey.encode("utf-8")
        AESkey = base64.b64decode(AESkey)
        cryptor = AES.new(AESkey, self.mode)
        cipherdata = cryptor.decrypt(msgContent_base64)
        cipherdata = cipherdata.decode()
        cipherdata = self.unpad(cipherdata)
        print("cipherdata is ", cipherdata)
        cipherdata = json.loads(cipherdata, encoding='utf-8')
        print("cipherdatalast is ", cipherdata)
        print("cipherdatalast'type", type(cipherdata))
        return cipherdata









msgContent = '7QBINUSFGGBAD+jfbEOcB5v5guqK3mKxDhtPH2waeDK5uJ0SkoczyaC2AgQoBL8untikw/5JU1mURct2SNVl8J5KsJZeuV4FI2xGkTlO/j+m5MPI44PGT2HkCml9O5hBzVzQ+72td85YrPuubEPl8EyjPDKDU8F95w6DwDOidHbxtofG4+JLgUQQgWZTzm9/QMpyS5jNADNiC5/GbktK8IB5wEyfdw7151sllB2Ry7n1EU9ip5BtATeAxDc1wPPj9RFPYqeQbQE3gMQ3NcDz4w=='
AESkey = 'lh46yd3exuscxevqhmdyzz'
new = Iot_encry_decry(msgContent,AESkey)
new.decry()