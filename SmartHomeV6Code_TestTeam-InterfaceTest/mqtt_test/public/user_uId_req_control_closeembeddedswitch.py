#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from mqtt_test.mqtt_bussiness.read_csv import Read_csv
import time
from mqtt_test.mqtt_bussiness import global_value


class User_uId_req_control_closeembeddedswitch(object):
    def __init__(self):
        pass

    def user_uId_req_control_closeembeddedswitch(self):
        read_csv = Read_csv('wl/user/uId/req_control_closeembeddedswitch')
        read_csv.mqtt_get_answer()
        return global_value.get_resultCode_value()


    def dispose(self):
        pass
