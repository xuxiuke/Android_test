#coding=utf-8

"""
作者: Duke
文件名: iot_sha256.py
创建时间: 2019/09/12-09:30
"""

import hashlib

def str_encrypt(str1):
    """
    使用sha256加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha256(str1)
    encrypts = sha.hexdigest()
    return encrypts

def md5(str1):
    m = hashlib.md5()
    m.update(str1.encode("utf-8"))
    return m.hexdigest()

# str1 = "12345@"
# print(md5(str1))