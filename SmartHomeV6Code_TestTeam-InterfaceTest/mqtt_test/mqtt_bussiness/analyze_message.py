#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import pickle
import json
from mqtt_test.mqtt_bussiness.iot_encry_decry import Iot_encry_decry



class Analyze_message(object):
    def __init__(self,msg,secretKey, secretuId):
        self.msg = msg
        self.secretKey = secretKey
        self.secretuId = secretuId

    def process_message(self):
        iot_encry_decry = Iot_encry_decry(self.msg, self.secretKey, self.secretuId)
        decry_data = iot_encry_decry.decry()
        return decry_data






















