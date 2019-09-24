# coding=utf-8

"""
作者: Duke
文件名: iot_get_msgContent_sianature.py
创建时间: 2019/09/12-09:25
"""

import base64
from Crypto.Cipher import AES
from public.cloud_iot.iot_base64 import Base64
from public.cloud_iot.iot_sha256 import str_encrypt
from public.cloud_iot import iot_sha256


class Iot_aes(object):
    def __init__(self, key, AESkey, nonce, timestamp, secretuId):
        self.key = key  # 必须是字符串
        self.AESkey = AESkey
        self.nonce = nonce
        self.timestamp = timestamp
        self.secretuId = secretuId
        self.mode = AES.MODE_ECB
        self.BS = AES.block_size  # 等于16
        # 补位
        self.pad = lambda s: s + ((self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode("utf-8"))

    # 由AESKey进行AES128加密，原内容不足16字节倍数的进行补充,补充字符串为缺少的字节个数；加密后对加密后字符进行base64编码
    # 加密函数，如果text不足16位就“用补充字符串为缺少的字节个数”补足为16位
    # 如果大于16当时不是16的倍数，那就补足为16的倍数
    # 正好16位就再补充一行16
    def get_msgContent(self):
        self.key = self.key.encode("utf-8")  # 先转换成字节
        # print(self.key)

        if not (len(self.key) % self.BS):
            new_data = self.key + (16 * chr(16)).encode("utf-8")
            # print(new_data)
        else:
            new_data = self.pad(self.key)
            # print(new_data)

        # 调用生成密钥的函数
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==
        AESkey = AESkey.encode("utf-8")
        AESkey = base64.b64decode(AESkey)
        cryptor = AES.new(AESkey, self.mode)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        cipherdata = cryptor.encrypt(new_data)
        base64_data = Base64(cipherdata)
        msgContent = base64_data.b64encode()
        # print(msgContent)   # 字符串
        return msgContent

    def get_signature(self):
        self.key = self.key.decode()  # 先转换成字节

        # 调用生成密钥的函数
        secretuId = iot_sha256.md5(self.secretuId)
        AESkey = self.AESkey + secretuId[-16:] + "=="  # 首先字符串拼接==

        list_signature = [self.nonce, self.timestamp, AESkey, self.get_msgContent()]
        list_signature.sort()
        signature_str = ''.join(list_signature)
        # print(signature_str)
        signature_bytes = signature_str.encode("utf-8")
        signature_encrypt = str_encrypt(signature_bytes)
        # print("sss", type(signature_encrypt))
        return signature_encrypt  # 字符串

        # generate_nonce = iot_generate_nonce()
        # timestamp = str(time.time())
        # echoStr = iot_get_AESkey()
        # iot_aes = Iot_aes(self.key)
        # msgContent = iot_aes.get_msgContent()      # 字符串
        # list_signature = [generate_nonce,timestamp,echoStr,msgContent]
        # list_signature = list_signature.sort()
        # signature_str = ''.join(list_signature)
        # signature_bytes = signature_str.encode("utf-8")
        # signature_encrypt = str_encrypt(signature_bytes)
        # return (signature_encrypt.decode())  #字符串

# iot = Iot_aes('diasdiausoidoasd')
# iot.encrypt()
