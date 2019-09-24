#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from mqtt_test.mqtt_bussiness.iot_base64 import Base64
import base64
from Crypto.Cipher import AES
import json
import demjson
from mqtt_test.mqtt_bussiness import iot_sha256



class Iot_encry_decry(object):
    def __init__(self, msg, AESkey, secretuId):
        self.msg = msg
        self.AESkey = AESkey
        self.secretuId = secretuId
        self.mode = AES.MODE_ECB
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def decry(self):
        # 直接传获取到的消息
        message = self.msg.decode()
        #print("message is ",message)
        getanswer = json.loads(message, encoding='utf-8')
        msgContent = getanswer['msgContent']
        msgContent_base64 = Base64(msgContent)
        msgContent_base64 = msgContent_base64.b64decode()
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==
        AESkey = AESkey.encode("utf-8")
        AESkey = base64.b64decode(AESkey)
        cryptor = AES.new(AESkey, self.mode)
        cipherdata = cryptor.decrypt(msgContent_base64)
        cipherdata = cipherdata.decode()
        cipherdata = self.unpad(cipherdata)
        cipherdata = json.loads(cipherdata, encoding='utf-8')
        return cipherdata










