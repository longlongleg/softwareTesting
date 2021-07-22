#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 14:30
# @Author : lumi
# @File : readConfig.py
# @Software: PyCharm
import configparser
from autoStruct.jingcaiAuto.tools import getFileDirectory

#读取config里面的数据
class ReadConfig:

    def __init__(self):
        self.filePath = getFileDirectory.get_directory(getFileDirectory.get_directory())+"\\config\\config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.filePath,encoding='utf-8')

    def get_data(self,section,key):
        return self.config.get(section,key)

    def get_list(self,section):
        return self.config.items(section)



if __name__ == '__main__':
    conf = ReadConfig()
    print(conf.get_data("host", "loginUrl"))
    print(conf.get_list("host"))

