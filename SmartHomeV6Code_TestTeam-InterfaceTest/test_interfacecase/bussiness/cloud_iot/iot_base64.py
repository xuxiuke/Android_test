#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import base64



class Base64(object):
    def __init__(self,string):
        self.string = string

    def b64encode(self):
        #bytesString = self.string.encode("utf-8")
        # base64 编码
        encodestr = base64.b64encode(self.string)
        #print(type(encodestr.decode()))
        return encodestr.decode()   #  decode()字节变成字符串

    def b64decode(self):
        bytesString = self.string.encode("utf-8")
        # base64 接码
        decodestr = base64.b64decode(self.string)
        #print(decodestr)
        return decodestr


# new = Base64(b'gLvBPuVlf5z6yfUgf1A3kn6PFEW3QGYZFWvNeZbD3Ow=')
# new.b64decode()