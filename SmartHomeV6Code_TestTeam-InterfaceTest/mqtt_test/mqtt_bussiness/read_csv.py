#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import random
import requests
import json
import csv
import urllib
import time
import base64
from  queue import  Queue
import  threading
from Crypto.Cipher import AES
from mqtt_test.mqtt_bussiness import sha1
from mqtt_test.mqtt_bussiness.open_csv import Read_file
from mqtt_test.mqtt_bussiness.iot_generate_nonce import iot_generate_nonce
from mqtt_test.mqtt_bussiness.iot_get_msgContent_sianature import Iot_aes
from mqtt_test.mqtt_bussiness.iot_get_return import iot_get_return
from mqtt_test.mqtt_bussiness.iot_encry_decry import Iot_encry_decry
from mqtt_test.mqtt_bussiness.iot_sha256 import str_encrypt
from mqtt_test.mqtt_bussiness.iot_base64 import Base64
from mqtt_test.mqtt_bussiness.get_client import Get_client
from mqtt_test.mqtt_bussiness.encry import Encry
from mqtt_test.mqtt_bussiness.message_control import Message_control
from mqtt_test.mqtt_bussiness.Queue_process_message import Producer,Consumer
from mqtt_test.mqtt_bussiness import global_value


class Read_csv(object):
    def __init__(self, key):
        self.key = key


    def read_csv(self):
        new = Read_file('demo_mqtt.csv')
        csv_dict = new.read_file()
        return csv_dict

    def mqtt_get_answer(self):
        get_return = iot_get_return()
        secretKey = get_return['date']['secretKey']  # 每个接口必须要传AESkey
        global_value.set_secretKey_value(secretKey)   #全局变量赋值

        user = get_return["data"]['mqttInfo']['user']
        passwd = get_return["data"]['mqttInfo']['passwd']
        host = get_return["data"]['mqttInfo']['host']
        port = get_return["data"]['mqttInfo']['port']
        port = int(port)

        csv_dict = Read_csv.read_csv(self)
        # 获取到的字符串格式数据转换成dict格式
        interface = json.loads(csv_dict[self.key], encoding='utf-8')
        global_value.set_interface_value(interface)
        topic = interface["topic"]
        topics = interface["topics"]
        topicsc = interface["topicsc"]
        answer = interface["answer"]
        cmd = interface["return_cmd"]
        global_value.set_return_cmd_value(cmd)  #全局变量赋值

        # 判断uId 和token 字符串
        if "uId" in topic:
            topic = topic.replace("uId", get_return["data"]['uId'])
        # print(topic)

        if "uId" in topics:
            topics = topics.replace("uId", get_return["data"]['uId'])
        # print(topics)

        if "uId" in topicsc:
            topicsc = topicsc.replace("uId", get_return["data"]['uId'])

        secretuId = get_return["data"]['uId']  # 每个接口必须要传uId
        global_value.set_secretuId_value(secretuId)   #全局变量赋值

        # 读取url的data
        data = interface["data"]
        if "token" in data:
            data["token"] = get_return["data"]['token']

        if "userID" in data:
            data["userID"] = get_return["data"]['uId']

        if "sceneID" in data:
            data["sceneID"] = global_value.get_return_sceneID_value()   # 全局变量return_sceneID

        if "roomID" in data:
            data["roomID"] = global_value.get_return_roomID_value()  # 全局变量return_roomID

        # if "sceneID" in data["data"][0]:
        #     data["data"][0]["sceneID" ] = global_value.get_return_sceneID_value()   # 全局变量return_sceneID

        generate_nonce = iot_generate_nonce()
        timestamp = time.time()
        timestamp = str(int(round(timestamp * 1000)))
        data = json.dumps(data)  # 字符串数据
        ercry_data = Encry(data,secretKey, generate_nonce,timestamp,secretuId)
        ercry_data = ercry_data.iot_encry_message()  #加密后要发送的消息 json格式
        message_control = Message_control(topic, topics,topicsc, ercry_data)
        get_client = Get_client(user,passwd,host,port)
        get_client = get_client.get_client(message_control)
        # 开始执行clinet
        get_client.loop_start()
        time.sleep(4)
        rc, mid = get_client.publish(topic, payload=json.dumps(ercry_data), qos=0)
        message_control.on_publish( rc)
        print("publish is ok")
        time.sleep(6)
        #会产生一个msg的参数字节形式的json,需要解密











