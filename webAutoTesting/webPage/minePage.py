#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/17 16:44
# @Author : lumi
# @File : minePage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By


from autoStruct.jingcaiAuto.webPage.login import Login


class MinePage():

    def __init__(self):
        self.login = Login()
        self.login.login()
        self.login.is_click(*(By.LINK_TEXT,'我的订单'))
        self.login.close_web()
        self.login.switch_window(0)

    def order_center(self,item):
        self.login.is_click(*(By.LINK_TEXT,item))
        self.login.url_change()
        assert self.login.ele_text(*(By.XPATH,'/html/body/div[4]/div[2]/h3')) == item



    def my_collection(self,item,expected):
        self.login.is_click(*(By.LINK_TEXT,item))
        self.login.url_change()
        assert self.login.ele_text(*(By.XPATH,'/html/body/div[4]/div[2]/h3')) == expected


    def customer_service(self,item,expected):
        self.login.is_click(*(By.LINK_TEXT,item))
        self.login.url_change()
        assert self.login.ele_text(*(By.XPATH,'/html/body/div[4]/div[2]/h3')) == expected


    def account_center(self,item,expected):
        self.login.is_click(*(By.LINK_TEXT,item))
        self.login.url_change()
        assert self.login.get_current_url() == expected

