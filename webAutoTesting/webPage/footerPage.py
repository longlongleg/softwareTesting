#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/16 17:04
# @Author : lumi
# @File : footerPage.py
# @Software: PyCharm

from selenium.webdriver.common.by import By


from autoStruct.jingcaiAuto.webPage.login import Login


class FooterPage():

    def __init__(self):
        self.login = Login()
        self.login.login()

    def click_brand(self,num):
        brand_list = self.login.get_eles(*(By.CLASS_NAME,'brand-item'))
        brand_list[num].click()
        self.login.is_new_window_open()
        self.login.switch_window(1)
        assert self.login.get_current_url() == "expected address"
        self.login.close_web()
        self.login.switch_window(0)

    def click_about_us(self,about_title):
        self.login.is_click(*(By.LINK_TEXT,about_title))
        self.login.switch_window(1)
        assert self.login.ele_text(*(By.XPATH,'/html/body/div[4]/div[2]/div/h1')) == about_title
        self.login.close_web()
        self.login.switch_window(0)


    def click_business_service(self,title,excepted):
        self.login.is_click(*(By.LINK_TEXT,title))
        self.login.switch_window(1)
        assert self.login.get_current_url() == excepted
        self.login.close_web()
        self.login.switch_window(0)
