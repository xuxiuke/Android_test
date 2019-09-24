#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from mqtt_test.mqtt_bussiness.iot_encry_decry import Iot_encry_decry
import time
import json
from  queue import  Queue
import  threading
from mqtt_test.mqtt_bussiness.Queue_process_message import Producer,Consumer
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.mqtt_bussiness.analyze_message import Analyze_message

class Message_control(object):
    def __init__(self,topic,topics,topicsc,msg):
        self.topic = topic
        self.topics = topics
        self.topicsc = topicsc
        self.msg = msg   #加密后的消息

    def on_message(self,client, userdata, msg):
        print("topic:" + msg.topic + ',' + " Message:" + str(msg.payload))
        msg = msg.payload  # 接受到的消息

        secretKey = global_value.get_secretKey_value()  # 全局变量secretKey
        secretuId = global_value.get_secretuId_value()  # 全局变量secretuId
        analyze_message = Analyze_message(msg, secretKey, secretuId)
        decry_data = analyze_message.process_message()  # 产生解密数据
        #print(decry_data)
        queue = Queue(32)
        consumer = Consumer(queue, '消费者',decry_data)
        producer = Producer(queue, '生产者',decry_data)
        producer.start()
        consumer.start()

        #
        # iot_encry_decry = Iot_encry_decry(message,self.secretKey)
        # decry_data = iot_encry_decry.decry()
        # global_value.set_decry_data_value(decry_data)
        # print(decry_data)
        # if "cmd" in decry_data:
        #     print("is ok")
        #     if decry_data["cmd"] == "504":
        #         print(decry_data["cmd"])
        #         receive_cmd504 = Receive_cmd504(decry_data,self.interface)
        #         result = receive_cmd504.receive_cmd504()
        #         print("result=",result)
        # else:
        #     print("data is fault")


        #time.sleep(99)
    #     client.on_message = message_control.on_message
    # def on_message2(self):
    #     print("123123")

    def on_publish(self, rc):  # 成功发布消息的操作
        self.msg = json.dumps(self.msg)
        if rc == 0:
            print("publish success, msg = " + self.msg)

    def on_connect(self,client, userdata, flags, rc):  # 连接后的操作 0为成功
        print("Connection returned " + str(rc))#client.subscribe(self.topic)
        client.subscribe(self.topics)
        client.subscribe(self.topicsc)