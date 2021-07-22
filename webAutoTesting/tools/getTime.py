#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 14:46
# @Author : lumi
# @File : getTime.py
# @Software: PyCharm

import time

def get_time():
     return time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())


print(get_time())