#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import hashlib

def str_encrypt(str):
    """
    使用sha256加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha256(str)
    encrypts = sha.hexdigest()
    return encrypts

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()

# str = "12345@"
# print(md5(str))



