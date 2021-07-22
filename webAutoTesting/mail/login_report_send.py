#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/14 11:08
# @Author : lumi
# @File : login_report_send.py
# @Software: PyCharm

from autoStruct.jingcaiAuto.tools.sendMail import SendMail
from autoStruct.jingcaiAuto.tools import getListValue
from autoStruct.jingcaiAuto.common.readConfig import ReadConfig

def login_report_send():

    mail = SendMail()
    config = ReadConfig()
    towho = getListValue.get_list_value(config.get_list("loginToWho"))
    subject = config.get_data("loginSendInfo", "subject")
    content = config.get_data("loginSendInfo", "content")
    attachment = config.get_data("loginSendInfo", "attachment")

    mail.send_mail(towho,subject,content,attachment)


login_report_send()