#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/14 16:34
# @Author : lumi
# @File : common_data.py
# @Software: PyCharm
from autoStruct.apiAuto.tool.operate_excel import OpExcel


class CommData:
    url_list = []
    header_list = []
    data_list = []
    method_list = []
    content_type_list = []

    def __init__(self, file_path, sheetname):
        self.excel = OpExcel(file_path, sheetname)
        self.max_row = self.excel.get_max_row()
        print(self.max_row)

    def get_url_list(self):

        for i in range(2, self.max_row + 1):
            self.url_list.append(self.excel.read_data(i, 1).strip())

        return self.url_list

    def get_header_list(self):

        for i in range(2, self.max_row + 1):
            data = self.excel.read_data(i, 3)
            if data == None:
                self.header_list.append(data)
            else:
                self.header_list.append(eval(data))

        return self.header_list

    def get_data_list(self):

        for i in range(2, self.max_row + 1):
            data = self.excel.read_data(i, 4)
            if data == None:

                self.data_list.append(data)
            else:
                self.data_list.append(eval(data))

        return self.data_list

    def get_methodlist(self):

        for i in range(2, self.max_row + 1):
            self.method_list.append(self.excel.read_data(i, 2))

        return self.method_list

    def get_contenttypelist(self):
        for i in range(2, self.max_row + 1):
            self.content_type_list.append(self.excel.read_data(i, 5))

        return self.content_type_list



"""
if __name__ == '__main__':
    com = CommData('../excel/request.xlsx','Sheet1')
    print(com.get_url_list())
    print(com.get_data_list())
    print(com.get_header_list())
    print(com.get_methodlist())


"""
