#coding=utf-8

"""
作者: Duke
文件名: read_csv.py
创建时间: 2019/09/11-17:18
"""

from public.open_file import Read_file


class Read_csv(object):

    @staticmethod
    def read_csv():
        read = Read_file('demo_cloud.csv')
        csv_dict = read.read_file()
        return csv_dict