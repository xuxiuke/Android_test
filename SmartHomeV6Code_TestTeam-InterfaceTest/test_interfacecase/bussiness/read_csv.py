# coding=utf-8


from test_interfacecase.bussiness.open_csv import Read_file


class Read_csv(object):

    @staticmethod
    def read_csv():
        read = Read_file('demo_cloud.csv')
        csv_dict = read.read_file()
        return csv_dict
