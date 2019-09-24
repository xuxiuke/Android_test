#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import random
from  queue import  Queue
import  threading
import time
from mqtt_test.mqtt_bussiness.analyze_message import Analyze_message
from mqtt_test.mqtt_bussiness import global_value
from mqtt_test.mqtt_bussiness.parse_data.receive_cmd import Receive_cmd

class Producer(threading.Thread):
    """
    @:param queue 阻塞队列
    @:param name 线程名字
    """
    def __init__(self,queue,name,msg):
        threading.Thread.__init__(self)
        self.queue = queue
        self.msg = msg
        self.name = name


    def run(self):
        self.queue.put(self.msg)
        print(self.name, '将', self.msg, '加入队列')
        time.sleep(3)
        #while True:




class Consumer(threading.Thread):
    def __init__(self,queue,name,msg):
        threading.Thread.__init__(self)
        self.queue = queue
        self.msg = msg
        self.name = name


    def run(self):
        while True:
            msg = self.queue.get(block=True, timeout=10)
            print (self.name,'将',msg,'从队列中移除')
            print(msg)  #解密后的数据

            interface = global_value.get_interface_value()   # 全局变量interface
            receive_cmd = Receive_cmd(msg,interface)
            if msg["cmd"] == global_value.get_return_cmd_value() and "cmd" in msg:
                result = eval("receive_cmd.""receive_cmd"+global_value.get_return_cmd_value()+"()")
                print("wonderful")
            self.queue.task_done()




