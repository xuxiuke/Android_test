#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import random
import ssl

import paho.mqtt.client as mqtt
from mqtt_test.mqtt_bussiness.message_control import Message_control

class Get_client(object):
    def __init__(self,user,passwd,host,port):
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port

    def get_client(self,message_control):
        client = mqtt.Client(clean_session=True, userdata=None, transport="tcp")
        _create_unverified_https_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        client.tls_set_context(context=_create_unverified_https_context)
        client.tls_insecure_set(True)
        client.username_pw_set(username= self.user, password=self.passwd)
        client.on_connect = message_control.on_connect
        client.on_message = message_control.on_message
        client.connect(self.host, self.port, 60)
        return client