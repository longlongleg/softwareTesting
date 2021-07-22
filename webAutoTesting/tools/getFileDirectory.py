#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 14:35
# @Author : lumi
# @File : getFileDirectory.py
# @Software: PyCharm

import os

def get_directory(file=__file__):
    return os.path.dirname(file)


#print(get_directory())