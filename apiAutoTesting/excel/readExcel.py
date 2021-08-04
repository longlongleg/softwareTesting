#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/8/3 20:23
# @Author : lumi
# @File : readExcel.py
# @Software: PyCharm
import openpyxl

class ReadExcel:

    def __init__(self,excel_path,sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name

    def get_data(self,row):
        workbook = openpyxl.load_workbook(self.excel_path)
        sh = workbook[self.sheet_name]
        #print(list(sh.rows))
        data = []
        for c in list(sh.rows)[row]:
            data.append(c.value)
        return data


if __name__ == '__main__':
    ex = ReadExcel('request.xlsx','Sheet1')
    print(ex.get_data(0))
    print(ex.get_data(1))
    print(ex.get_data(2))
    print(ex.get_data(3))
    print(ex.get_data(4))



