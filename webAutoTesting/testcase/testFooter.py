#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/17 14:39
# @Author : lumi
# @File : testFooter.py
# @Software: PyCharm
import os

import allure
import pytest

from autoStruct.jingcaiAuto.webPage.footerPage import FooterPage



class TestFooter:

    def setup_class(self):
        self.footer = FooterPage()


    @allure.feature("点击底部优质品牌商图片")
    @allure.story("优质品牌商链接")
    @allure.step("下滑到底部，点击图片，直到品牌商网站")
    @allure.description("测试点击底部的品牌商图片，跳转链接功能")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('num',[2,3,4])
    def test_brand(self,num):
        self.footer.click_brand(num)

    @allure.feature("点击底部关于我们")
    @allure.story("关于我们每个点测试")
    @allure.step("下滑到底部，点击关于我们下面的链接")
    @allure.description("测试点击底部的关于我们的各个链接点")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('about_title', ['鲸采电酷简介', '如何开店', '常见问题'])
    def test_about_us(self, about_title):
        self.footer.click_about_us(about_title)

    @allure.feature("点击底部商务与服务")
    @allure.story("商务与服务每个链接点击")
    @allure.step("下滑到底部，点击商务与服务下面的链接")
    @allure.description("测试点击底部的商务与服务的各个链接点")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('title,expected', [('提供优质产品','expected address'),('加入渠道分销','expected address'),('售后保障','expected address'),('支付方式','expected address')])
    def test_business_service(self, title,expected):
        self.footer.click_business_service(title,expected)







if __name__ == '__main__':

    pytest.main(['-vs',"testFooter.py","--alluredir","../report/footer_report/allure-result"])
    os.system(r"allure generate --clean ../report/footer_report/allure-result -o ../report/footer_report/allure-report")