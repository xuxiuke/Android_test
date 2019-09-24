#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import time
import requests
import base64
from Crypto.Cipher import AES
from test_interfacecase.bussiness.cloud_iot.iot_base64 import Base64
from test_interfacecase.bussiness.cloud_iot import iot_sha256
from test_interfacecase.bussiness.cloud_iot.iot_sha256 import str_encrypt


class Iot_aes(object):
    def __init__(self,key,AESkey,nonce,timestamp,secretuId):
        self.key = key                 # 必须是字符串
        self.AESkey = AESkey
        self.nonce = nonce
        self.timestamp = timestamp
        self.secretuId = secretuId
        self.mode = AES.MODE_ECB
        self.BS = AES.block_size     # 等于16
        # 补位
        self.pad = lambda s: s + ((self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode("utf-8"))

    #由AESKey进行AES128加密，原内容不足16字节倍数的进行补充,补充字符串为缺少的字节个数；加密后对加密后字符进行base64编码
    # 加密函数，如果text不足16位就“用补充字符串为缺少的字节个数”补足为16位
    # 如果大于16当时不是16的倍数，那就补足为16的倍数
    #正好16位就再补充一行16
    def get_msgContent(self):
        self.key = self.key.encode("utf-8")   #先转换成字节

        if not(len(self.key) % self.BS):
            new_data = self.key + ( 16 * chr(16)).encode("utf-8")

        else:
            new_data = self.pad(self.key)


        #调用生成密钥的函数
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==
        AESkey= AESkey.encode("utf-8")
        AESkey = base64.b64decode(AESkey)
        cryptor = AES.new(AESkey, self.mode)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        cipherdata = cryptor.encrypt(new_data)
        base64_data = Base64(cipherdata)
        msgContent = base64_data.b64encode()
        return msgContent


    def get_signature(self):
        self.key = self.key.decode()  # 先转换成字节
        # 调用生成密钥的函数
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==

        list_signature = [self.nonce, self.timestamp, AESkey, self.get_msgContent()]
        list_signature.sort()
        signature_str = ''.join(list_signature)
        signature_bytes = signature_str.encode("utf-8")
        signature_encrypt = str_encrypt(signature_bytes)
        return (signature_encrypt)  #字符串



