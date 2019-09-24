# coding=utf-8

"""
作者: Duke
文件名: open_file.py
创建时间: 2019/09/11-17:21
"""

import csv


class Read_file(object):

    def __init__(self, file):
        self.file = file

    def read_file(self):
        path = "D:\\test\\test_interface\date"
        with open(path + "\\" + self.file, 'r', encoding="utf-8") as myFile:
            csv_rows = {}
            rows = csv.DictReader(myFile)  # DictReader 以字典形式读取
            for row in rows:
                key = row['key']
                csv_rows[key] = row["value"]  # 打印出列
            return csv_rows
