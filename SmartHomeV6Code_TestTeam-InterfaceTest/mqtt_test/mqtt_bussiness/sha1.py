#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import hashlib

def str_encrypt(str):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts