#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 18:15
# @Author : lumi
# @File : getListData.py
# @Software: PyCharm

import getFileDirectory
def get_data(filename):

    file_path = getFileDirectory.get_directory(getFileDirectory.get_directory())+"\\data\\"+filename
    f = open(file_path,'r',encoding='utf-8')
    list = []
    items = f.readlines()
    for item in items:

        list.append(item.strip())

    return list



