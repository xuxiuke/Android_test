#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import json
import time
from mqtt_test.mqtt_bussiness.iot_encry_decry import Iot_encry_decry
from mqtt_test.mqtt_bussiness import global_value


class Receive_cmd(object):
    def __init__(self, decry_data, interface):
        self.decry_data = decry_data
        self.interface = interface

    def receive_cmd504(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data["data"][0]:
                new_list.append(i)
            new_list.sort()
            for j in self.decry_data["data"]:
                if j["name"] == "test123":
                    return_sceneID = j["sceneID"]
                    global_value.set_return_sceneID_value(return_sceneID)  # 全局变量赋值

                if j["name"] == "test123456":
                    return_sceneID = j["sceneID"]
                    global_value.set_return_sceneID_value(return_sceneID)  # 全局变量赋值

            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd502(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd500(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)

            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
            elif new_list == self.interface["answers"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值

            return resultCode


    def receive_cmd503(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd505(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode


    def receive_cmd506(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data["data"][0]:
                new_list.append(i)
            new_list.sort()
            for j in self.decry_data["data"]:
                if j["name"] == "理查test123":
                    return_roomID = j["roomID"]
                    global_value.set_return_roomID_value(return_roomID)  # 全局变量赋值

                if j["name"] == "理查基娜test123":
                    return_roomID = j["roomID"]
                    global_value.set_return_roomID_value(return_roomID)  # 全局变量赋值

            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd511(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd512(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd513(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode

    def receive_cmd514(self):
        new_list = []
        if self.interface["data"]["gwID"] == self.decry_data["gwID"]:
            for i in self.decry_data:
                new_list.append(i)
            new_list.sort()
            print(new_list)
            if new_list == self.interface["answer"]:
                resultCode = "0"
                global_value.set_resultCode_value(resultCode)  # 全局变量赋值
                return resultCode