#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/16 17:03
# @Author : lumi
# @File : headerPage.py
# @Software: PyCharm
import time

from selenium.webdriver.common.by import By

from autoStruct.jingcaiAuto.webPage.login import Login


class HeaderPage():

    def __init__(self):
        self.login = Login()
        self.login.login()

    def click_my_order(self):
        self.login.is_click(*(By.LINK_TEXT,'我的订单'))
        self.login.is_new_window_open()
        self.login.switch_window(1)
        assert self.login.get_current_url() == "expected address"
        self.login.close_web()
        self.login.switch_window(0)



    def click_vip_center(self):
        self.login.is_click(*(By.LINK_TEXT,'会员中心'))
        self.login.url_change()
        assert self.login.get_current_url() == "expected address"
        self.login.web_back_to()


    def move_to_jingcaidianku(self):
        self.login.move_to_ele(*(By.CLASS_NAME,'menubox'))
        assert self.login.is_ele((By.XPATH,'/html/body/div[1]/div/ul[2]/li[4]/div/div[2]/img'))

    def move_to_customer_service(self):
        self.login.move_to_ele(*(By.XPATH,'/html/body/div[1]/div/ul[2]/li[5]/div'))
        assert self.login.is_ele((By.CLASS_NAME,'item'))



    def click_store_settled(self):
        self.login.is_click(*(By.LINK_TEXT,'商家入驻'))
        self.login.is_new_window_open()
        self.login.switch_window(1)
        assert self.login.get_current_url()=="expected address"
        self.login.close_web()
        self.login.switch_window(0)


    def click_store_login(self):
        self.login.is_click(*(By.LINK_TEXT,'商家登录'))
        self.login.is_new_window_open()
        self.login.switch_window(1)
        assert self.login.get_current_url()=="expected address"
        self.login.close_web()
        self.login.switch_window(0)


    def click_contact_us(self):
        self.login.is_click(*(By.LINK_TEXT,'联系我们'))
        self.login.is_new_window_open()
        self.login.switch_window(1)
        assert self.login.ele_text(*(By.CLASS_NAME,'arrow')) == "联系我们400-852-8980"
        self.login.close_web()
        self.login.switch_window(0)

    def click_exit(self):
        self.login.is_click(*(By.LINK_TEXT,'退出'))
        assert self.login.get_current_url()=="expected address"


    def web_quit(self):
        self.login.quit_web()




