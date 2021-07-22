#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/14 14:48
# @Author : lumi
# @File : testHome.py
# @Software: PyCharm
import os
import time

import allure
import pytest
from selenium.webdriver.common.by import By
from autoStruct.jingcaiAuto.log.log import Logger
from autoStruct.jingcaiAuto.webPage.homePage import HomePage


logger = Logger(logger='TestHome').getlog()
class TestHome:

    def setup_class(self):
        self.home = HomePage()
        self.home.login()
        self.home.ele_visiable((By.LINK_TEXT,'首页'))
        self.home.shouye_click()
        logger.info("登录后点击首页来到首页页面")

    @allure.feature("鼠标移动到分类")
    @pytest.mark.run(order=1)
    @allure.description("将鼠标移动到左边的分类，显示分类项")
    @pytest.mark.parametrize("category,class_att,num",[('宠物周边产品','list-cashcade forel  cate-item-hover  hover',0),('手机配件类','list-cashcade forel  cate-item-hover  hover',1),('电脑数码配件','list-cashcade forel  cate-item-hover  hover',2),('智能家居娱乐','list-cashcade forel  hover',5)])
    def test_move_to_category(self,category,class_att,num):
        self.home.move_to_category(category)
        logger.info("鼠标移动到左边分类")
        ele_list = self.home.get_eles(*(By.CLASS_NAME,'list-cashcade'))
        assert ele_list[num].get_attribute("class") == class_att
        time.sleep(1)

    @allure.feature("鼠标移动到翻页数字")
    @pytest.mark.run(order=2)
    @allure.description("将鼠标移动到翻页的数字，显示对应的轮播图图片")
    @pytest.mark.parametrize('num',[1,2,3])
    def test_move_to_num(self,num):
        ele_list = self.home.move_to_num(num)
        logger.info("鼠标移动到首页轮播图数字")
        assert ele_list[num].get_attribute("class") == "bullet on"

    @allure.feature("鼠标点击分类")
    @pytest.mark.run(order=3)
    @allure.description("点击左边的分类，跳转到对应的商品显示页面")
    @pytest.mark.parametrize('category', ['宠物周边产品', '手机配件类', '个人护理美容类'])
    def test_click_category(self, category):
        self.home.click_category(category)
        self.home.switch_window(1)
        assert self.home.ele_text(*(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/span/div')) == category
        self.home.close_web()
        self.home.switch_window(0)
        time.sleep(1)

    @allure.feature("点击首页翻转图右边的新品图片")
    @pytest.mark.run(order=10)
    @allure.description("点击右边的新品图片，跳转到对应的产品介绍页面")
    @pytest.mark.parametrize('xpath',['//*[@id="NavSort"]/div/div[2]/a[1]','//*[@id="NavSort"]/div/div[2]/a[2]'])
    def test_click_new_arrival(self,xpath):
        self.home.click_new_arrival(xpath)
        self.home.url_change()
        self.home.refresh_web()
        #assert self.home.url_change()
        self.home.web_back_to()
        time.sleep(1)

    @allure.feature("输入搜索内容")
    @pytest.mark.run(order=5)
    @allure.description("在输入框输入搜索内容，显示对应的产品")
    @pytest.mark.parametrize('search_goods',['口红','手机','风扇','智能'])
    def test_input_search_goods(self, search_goods):
        self.home.search_goods(search_goods)
        assert self.home.ele_text(*(By.XPATH,'/html/body/div[4]/div/div/div/div[2]'))==search_goods
        self.home.web_back_to()
        time.sleep(1)

    @allure.feature("点击热门搜索")
    @pytest.mark.run(order=6)
    @allure.description("点击输入框下面的热门搜索，跳转到对应的产品列表页面")
    @pytest.mark.parametrize('hot_search', ['暖手宝', '电动牙刷', '挂烫机', '洗脸仪'])
    def test_hot_search(self, hot_search):
        self.home.click_hot_search(hot_search)
        self.home.switch_window(1)
        assert self.home.ele_text(*(By.XPATH, '/html/body/div[4]/div/div/div/div[2]')) == hot_search
        self.home.close_web()
        self.home.switch_window(0)
        time.sleep(1)

    @allure.feature("点击鲸采好物推荐")
    @pytest.mark.run(order=7)
    @allure.description("点击下方的产品推荐，跳转到对应的产品详情页面")
    @pytest.mark.parametrize('goods_recommend', ['鲸采新品夏季手持风扇 小巧便携二合一可折叠无线充风扇挂脖', '鲸采2021年新品熨斗 居家衣物熨烫机 无线电熨斗蒸汽熨烫', '多功能蓝牙音箱充电宝手电筒台灯七彩氛围灯自拍杆音响', 'TF口红'])
    def test_goods_recommend(self, goods_recommend):
        self.home.click_goods_recommend(goods_recommend)
        self.home.switch_window(1)
        assert self.home.get_url_title() == goods_recommend+" 鲸采电酷新品"
        self.home.close_web()
        self.home.switch_window(0)
        time.sleep(1)

    @allure.feature("点击鲸采好物推荐各栏目的 更多")
    @pytest.mark.run(order=8)
    @allure.description("点击首页好物推荐各栏目的 更多选项")
    @pytest.mark.parametrize('num', [0,3])
    def test_more(self, num):
        self.home.click_more(num)

    def teardown_class(self):
        time.sleep(3)
        self.home.quit_web()






if __name__ == '__main__':

    pytest.main(['-vs','testHome.py','--html=../report/home_report/home_report.html','--alluredir=../report/home_report/allure-result'])
    os.system('allure generate ../report/home_report/allure-result -o ../report/home_report/home_report.html --clean')
    #pytest.main(['-vs', 'testHome.py', '--html=../report/home_report/home_report.html', '--self-contained-html'])