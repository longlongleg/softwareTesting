#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/14 14:48
# @Author : lumi
# @File : homePage.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from autoStruct.jingcaiAuto.common.readConfig import ReadConfig
from autoStruct.jingcaiAuto.page.webElement import WebElement
from autoStruct.jingcaiAuto.tools import getCode
from autoStruct.jingcaiAuto.webPage.loginPage import LoginPage


class HomePage(WebElement):

    def __init__(self):
        self.driver = webdriver.Chrome()
        WebElement.__init__(self, self.driver)
        readConfig = ReadConfig()
        login_url = readConfig.get_data("host", "loginUrl")
        self.get_url(login_url)


    def login(self):
        self.send_key('account',*(By.ID,'name'))
        self.send_key('pwd',*(By.ID,'setPassword'))
        self.send_key(getCode.get_code(self.driver,'//*[@id="code_img"]'),*(By.ID,'verifyCode'))
        time.sleep(3)
        self.is_click(*(By.XPATH,'//*[@id="loginButton"]/div/div'))

    def shouye_click(self):
        self.is_click(*(By.LINK_TEXT,'首页'))

    def move_to_category(self,text):
        self.move_to_ele(*(By.LINK_TEXT,text))

    def click_category(self,text):
        self.is_click(*(By.LINK_TEXT,text))

    def move_to_num(self,num):
        list = self.get_eles(*(By.CLASS_NAME,'bullet'))
        self.move_to_ele2(list[num])
        return list

    def search_goods(self,search_good):
        self.send_key(search_good,*(By.ID,'keyword'))
        self.is_click(*(By.CLASS_NAME,'button'))

    def click_hot_search(self,hot_key):
        self.is_click(*(By.LINK_TEXT,hot_key))

    def click_goods_recommend(self,goods_link):
        self.is_click(*(By.PARTIAL_LINK_TEXT,goods_link))

    def click_more(self,num):
        more_list = self.get_eles(*(By.CLASS_NAME,'more'))
        print(len(more_list))

        more_list[num].click()
        self.web_back_to()



    def click_new_arrival(self,xpath):
        self.is_click(*(By.XPATH,xpath))
