#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 14:53
# @Author : lumi
# @File : sendMail.py
# @Software: PyCharm
from autoStruct.jingcaiAuto.common.readConfig import ReadConfig
from autoStruct.jingcaiAuto.tools import getListValue
import yagmail

class SendMail:
    def __init__(self):
        config = ReadConfig()
        host = config.get_data("mailHost","host")
        account = config.get_data("mailHost","account")
        pwd = config.get_data("mailHost","password")


        self.mail = yagmail.SMTP(account,pwd,host)

    def send_mail(self,towho,subject,content,attachment=None):
        self.mail.send(towho,subject,content,attachment)



if __name__ == '__main__':
    mail = SendMail()
    mail.send_mail()