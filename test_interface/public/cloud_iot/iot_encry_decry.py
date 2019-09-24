#coding=utf-8

"""
作者: Duke
文件名: iot_encry_decry.py
创建时间: 2019/09/12-09:39
"""

import base64
from Crypto.Cipher import AES
import json
from public.cloud_iot import iot_sha256


class Iot_encry_decry(object):
    def __init__(self,msgContent,AESkey, secretuId):
        self.msgContent = msgContent
        self.AESkey = AESkey
        self.mode = AES.MODE_ECB
        self.secretuId = secretuId
        self.unpad = lambda s: s[0:-ord(s[-1])]

    def decry(self):
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==
        AESkey = AESkey.encode("utf-8")
        AESkey = base64.b64decode(AESkey)
        cryptor = AES.new(AESkey, self.mode)
        cipherdata = cryptor.decrypt(self.msgContent)
        cipherdata = cipherdata.decode()
        cipherdata = self.unpad(cipherdata)
        cipherdata = json.loads(cipherdata, encoding='utf-8')
        print(cipherdata)
        return cipherdata