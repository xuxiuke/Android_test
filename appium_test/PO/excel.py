# coding=utf-8

"""
Created on 2018年8月15日

@author: Duke   把excel中的数据读取为字典并使用，用于在Excel中保存控件库
"""

import xlrd

excel_path = 'D:\\test\\appium_test\date\ControlLibrary.xlsx'
dict1 = {}


# ID
def id_con(text):
    date = xlrd.open_workbook(excel_path)
    table = date.sheets()[0]
    rows = table.nrows
    cols = table.ncols

    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict1[title] = value
    return dict1[text]


# xpath
def xpath_con(text):
    date = xlrd.open_workbook(excel_path)
    table = date.sheets()[1]
    rows = table.nrows
    cols = table.ncols

    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict1[title] = value
    return dict1[text]


# activity
def activity_con(text):
    date = xlrd.open_workbook(excel_path)
    table = date.sheets()[2]
    rows = table.nrows
    cols = table.ncols

    for i in range(0, rows):
        for j in range(cols):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            dict1[title] = value
    return dict1[text]
