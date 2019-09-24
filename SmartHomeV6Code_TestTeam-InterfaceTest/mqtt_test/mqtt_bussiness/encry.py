#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import time
import json
from mqtt_test.mqtt_bussiness import iot_base64
from mqtt_test.mqtt_bussiness import iot_sha256
from mqtt_test.mqtt_bussiness import iot_get_return
from mqtt_test.mqtt_bussiness.iot_generate_nonce import iot_generate_nonce
from mqtt_test.mqtt_bussiness.iot_get_msgContent_sianature import Iot_aes



class Encry(object):
    def __init__(self,data,secretKey,generate_nonce,timestamp,secretuId):
        self.data = data
        self.secretKey = secretKey
        self.generate_nonce = generate_nonce
        self.timestamp = timestamp
        self.secretuId = secretuId

    def iot_encry_message(self):
        #generate_nonce = iot_generate_nonce()
        data = json.dumps(self.data)
        iot_aes = Iot_aes(self.data,self.secretKey, self.generate_nonce, self.timestamp, self.secretuId)
        msgContent = iot_aes.get_msgContent()
        signature = iot_aes.get_signature()
        message = {"signature": signature, "nonce": self.generate_nonce, "timestamp": self.timestamp, "msgContent": msgContent}
        return message