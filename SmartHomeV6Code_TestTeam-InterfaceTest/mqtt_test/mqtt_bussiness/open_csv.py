#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import json
import csv
import os


class Read_file(object):
    def __init__(self, file):
        self.file = file

    def read_file(self):
        '''
        with open('demo_cloud.csv', 'rb') as myFile:
            rows = csv.reader(myFile)
            for row in rows:
                print row  # 打印出列    '''
        #path = os.path.dirname(os.getcwd())  # cmd 执行路径   以及用例单独执行
        # path = os.getcwd()             #ide 执行路径
        path="D:\\code\SmartHomeV6Code_TestCloud\\mqtt_test"
        with open( path + "\\"+self.file, 'r') as myFile:
            csv_rows = {}
            rows = csv.DictReader(myFile)
            for row in rows:
                key = row['key']
                csv_rows[key] = row["value"]  # 打印出列
            return csv_rows



# new = Read_file('demo_cloud.csv')
# new.read_file()














