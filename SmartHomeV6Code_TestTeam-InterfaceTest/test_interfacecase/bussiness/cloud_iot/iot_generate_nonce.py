#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import random
def iot_generate_nonce():
    ''' 随机生成6位的随机数 '''
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(97, 123): # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
    generate_nonce = ''.join(myslice) # list to string
    # print (code_list)
    # print (type(myslice))
    # print(generate_nonce)
    # print(type(generate_nonce))
    return generate_nonce

# iot_generate_nonce()