#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 17:11
# @Author : lumi
# @File : loginPage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from autoStruct.jingcaiAuto.page.webElement import WebElement
from autoStruct.jingcaiAuto.common.readConfig import ReadConfig
from selenium import webdriver
from autoStruct.jingcaiAuto.tools import getCode


class LoginPage(WebElement):

    def __init__(self):
        self.driver = webdriver.Chrome()
        WebElement.__init__(self,self.driver)
        readConfig = ReadConfig()
        login_url = readConfig.get_data("host","loginUrl")
        self.get_url(login_url)

    def account_clear(self):
        self.is_clear(*(By.ID,'name'))

    def password_clear(self):
        self.is_clear(*(By.ID, 'setPassword'))

    def code_clear(self):
        self.is_clear(*(By.ID, 'verifyCode'))

    def send_account(self,account):
        self.send_key(account,*(By.ID,'name'))

    def send_password(self,pwd):
        self.send_key(pwd,*(By.ID,'setPassword'))

    def send_code(self):
        code = getCode.get_code(self.driver,'//*[@id="code_img"]')
        self.send_key(code,*(By.ID,'verifyCode'))

    def btn_click(self):
        self.is_click(*(By.XPATH,'//*[@id="loginButton"]/div/div'))

    def forget_password(self):
        self.is_click(*(By.LINK_TEXT,'忘记密码？'))

    def register_right_now(self):
        self.is_click(*(By.LINK_TEXT,'立即注册'))

    def web_back(self):
        self.web_back_to()

    def web_quit(self):
        self.close_web()

