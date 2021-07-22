#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 16:04
# @Author : lumi
# @File : webElement.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class WebElement:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def get_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(2)


    def get_ele(self,*loc):
        return self.driver.find_element(*loc)

    def get_eles(self,*loc):
        return self.driver.find_elements(*loc)

    def is_click(self,*loc):
        self.get_ele(*loc).click()

    def send_key(self,text,*loc):
        self.get_ele(*loc).send_keys(text)

    def is_clear(self,*loc):
        self.get_ele(*loc).clear()

    def switch_window(self,num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def switch_frame(self,*loc):
        self.driver.switch_to.frame(self.get_ele(*loc))

    def switch_alert(self):
        return self.driver.switch_to.alert

    def alert_accept(self):
        self.switch_alert().accept()

    def alert_deny(self):
        self.switch_alert().dismiss()

    def ele_visiable(self,loc):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(loc))

    def url_change(self):
        WebDriverWait(self.driver,5).until(EC.url_changes)

    def is_ele(self,*loc):
        flag = True

        try:
            self.get_ele(*loc)
            return flag
        except:
            flag=False
            return flag

    def ele_text(self,*loc):
        return self.get_ele(*loc).text

    def get_current_url(self):
        return self.driver.current_url

    def close_web(self):
        self.driver.close()

    def quit_web(self):
        self.driver.quit()

    def web_back_to(self):
        self.driver.back()

    def web_forward_to(self):
        self.driver.forward()

    def get_ele_att(self,att,*loc):
        return self.get_ele(*loc).get_attribute(att)

    def move_to_ele(self,*loc):
        ActionChains(self.driver).move_to_element(self.get_ele(*loc)).perform()

    def move_to_ele2(self,ele):
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_url_title(self):
        return self.driver.title

    def refresh_web(self):
        self.driver.refresh()

    def is_new_window_open(self):
        WebDriverWait(self.driver,5).until(EC.new_window_is_opened)

    def is_alert(self):
        flag=True
        try:
            EC.alert_is_present()
            return flag
        except:
            flag=False
            return flag



if __name__ == '__main__':
    driver = WebElement(webdriver.Chrome())
    driver.get_url("https://www.baidu.com")
    driver.is_click(*(By.LINK_TEXT,'新闻'))
    driver.switch_window(1)
    driver.send_key('科技',*(By.ID,'ww'))






