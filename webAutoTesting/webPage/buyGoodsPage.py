#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/19 9:55
# @Author : lumi
# @File : buyGoodsPage.py
# @Software: PyCharm
import time

import selenium.webdriver.remote.utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from autoStruct.jingcaiAuto.page.webElement import WebElement
from autoStruct.jingcaiAuto.webPage.login import Login


class BuyGoodsPage(WebElement):

    def __init__(self):
        self.login = Login()
        self.login.login()

    def choose_goods(self,goods):
        self.login.is_click(*(By.LINK_TEXT,goods))
        self.login.is_new_window_open()
        self.login.switch_window(1)

    def presale_btn(self):
        self.login.ele_visiable((By.CLASS_NAME,'btn-presale'))
        self.login.is_click(*(By.CLASS_NAME,'btn-presale'))

    def choose_style_counts(self):
        self.login.is_click(*(By.XPATH,'//*[@id="destine"]/div[1]/div[2]/ul/li[1]'))
        self.login.is_click(*(By.XPATH,'//*[@id="destine"]/div[2]/div[2]/span[1]'))
        n=1
        self.login.send_key(n,*(By.NAME,'planvalue104'))

        #counts_ele[1].send_keys(num)
        self.login.is_click(*(By.XPATH,'//*[@id="destine"]/div[2]/div[2]/span[2]'))
        while(self.login.is_ele(*(By.ID,'popup_container'))):
            self.login.is_click(*(By.ID,'popup_ok'))
            n+=1
            self.login.is_clear(*(By.NAME,'planvalue104'))
            self.login.send_key(n,*(By.NAME,'planvalue104'))
            self.login.is_click(*(By.XPATH,'//*[@id="destine"]/div[2]/div[2]/span[2]'))

        self.login.send_key(n, *(By.NAME, 'planvalue105'))
        self.login.is_click(*(By.CLASS_NAME,'buynow'))






    def add_num(self):
        self.login.ele_visiable((By.CLASS_NAME,'jia'))
        self.login.is_click(*(By.CLASS_NAME,'jia'))
        self.login.is_click(*(By.CLASS_NAME,'buynow'))
        print(self.login.is_ele((By.ID, 'popup_container')))

        while (self.login.is_ele(*(By.ID,'popup_container'))):
            
            self.login.is_click(*(By.ID,'popup_ok'))
            self.login.is_click(*(By.CLASS_NAME, 'jia'))
            self.login.is_click(*(By.CLASS_NAME, 'buynow'))

        assert self.login.get_current_url() == 'expected address'


    def change_address(self):
        self.login.is_click(*(By.XPATH,'//*[@id="consigneeItemAllClick"]/span'))
        address_list = self.login.get_eles(*(By.CLASS_NAME,'consignee-item'))
        address_list[0].click()



    def buy_and_pay(self):
        self.login.is_click(*(By.ID,'order-submit'))
        self.login.is_click(*(By.ID,'selectOrderBalance'))
        self.login.send_key('123456',*(By.ID,'balancePassword'))
        self.login.is_click(*(By.ID,'PayButtom'))
        assert self.login.is_ele(*(By.LINK_TEXT,'订单中心'))
        self.login.close_web()
        self.login.switch_window(0)

    def presale_buy_and_pay(self):
        Select(self.login.get_ele(*(By.ID,'deliveryDaySelect'))).select_by_visible_text('15')
        self.login.is_click(*(By.ID,'checkservice'))
        self.login.is_click(*(By.ID,'order-submit'))
        self.login.is_click(*(By.ID, 'selectOrderBalance'))
        self.login.send_key('123456', *(By.ID, 'balancePassword'))
        self.login.is_click(*(By.ID, 'PayButtom'))
        assert self.login.is_ele(*(By.LINK_TEXT, '订单中心'))
        self.login.close_web()
        self.login.switch_window(0)

