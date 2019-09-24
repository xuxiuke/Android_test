#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import csv
import urllib
import requests
from  test_interfacecase.bussiness.kernal_function import Kernal_function
import json
from  test_interfacecase.bussiness import get_serveraddress
from urllib import parse,request
from  test_interfacecase.bussiness.cloud_iot.iot_get_return import iot_get_return
from  test_interfacecase.bussiness.cloud_iot.iot_base64 import Base64
from  test_interfacecase.bussiness.cloud_iot.iot_encry_decry import Iot_encry_decry

class Users_uId_devices(object):
    def __init__(self):
        pass

    def users_uId_devices(self):

        read_csv = Kernal_function('users/uId/devices')
        return read_csv.iot_get_answer()["resultCode"]



    def dispose(self):
        pass
