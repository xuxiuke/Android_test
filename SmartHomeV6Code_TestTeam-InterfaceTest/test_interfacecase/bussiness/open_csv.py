# coding=utf-8

import csv


class Read_file(object):

    def __init__(self, file):
        self.file = file

    def read_file(self):
        path = "D:\\test\SmartHomeV6Code_TestTeam-InterfaceTest\\test_interfacecase"
        with open(path + "\\" + self.file, 'r', encoding="utf-8") as myFile:
            csv_rows = {}
            rows = csv.DictReader(myFile)  # DictReader 以字典形式读取
            for row in rows:
                key = row['key']
                csv_rows[key] = row["value"]  # 打印出列
            return csv_rows
