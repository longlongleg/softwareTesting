#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/16 17:22
# @Author : lumi
# @File : login.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from autoStruct.jingcaiAuto.common.readConfig import ReadConfig
from autoStruct.jingcaiAuto.page.webElement import WebElement
from autoStruct.jingcaiAuto.tools import getCode


class Login(WebElement):

    def __init__(self):
        self.driver = webdriver.Chrome()
        WebElement.__init__(self, self.driver)
        readConfig = ReadConfig()
        login_url = readConfig.get_data("host", "loginUrl")
        self.get_url(login_url)

    def login(self):
        self.send_key('account', *(By.ID, 'name'))
        self.send_key('pwd', *(By.ID, 'setPassword'))
        self.send_key(getCode.get_code(self.driver, '//*[@id="code_img"]'), *(By.ID, 'verifyCode'))
        time.sleep(3)
        self.is_click(*(By.XPATH, '//*[@id="loginButton"]/div/div'))
        self.is_click(*(By.LINK_TEXT, '首页'))



