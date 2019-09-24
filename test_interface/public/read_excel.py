# coding=utf-8

"""
作者: Duke
文件名: read_excel.py
创建时间: 2019/09/16-16:25
"""

import xlrd

excel_path = 'D:\\test\\test_interface\date\iot_cloud.xlsx'
dict1 = {}


def iot_cloud(key):
    date = xlrd.open_workbook(excel_path)  # 打开文件
    table = date.sheets()[0]  # 第一页
    rows = table.nrows  # 排
    cols = table.ncols  # 列

    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict1[title] = value
    return dict1[key]


if __name__ == '__main__':  # 测试一下代码
    data_list = iot_cloud('login/byemail')
    print(data_list)
