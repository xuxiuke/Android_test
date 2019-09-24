# coding=utf-8

import csv


class readFile(object):
    def __init__(self, file):
        self.file = file

    def readfile(self):
        path = "D:\\code\SmartHomeV6Code_TestCloud\\test_interfacecase\\"
        with open(path + self.file, "r", encoding="utf-8") as myFile:
            csvRow = {}
            rows = csv.DictReader(myFile)
            for row in rows:
                key = row["key"]
                csvRow[key] = row["value"]
            return csvRow

# r=readFile("demo_cloud.csv")
# a=r.readfile()
# print(a["login/bythird"])
