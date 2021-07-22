#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/16 18:07
# @Author : lumi
# @File : testHeader.py
# @Software: PyCharm
import os

import allure
import pytest

from autoStruct.jingcaiAuto.webPage.headerPage import HeaderPage


class TestHeader:

    def setup_class(self):
        self.header = HeaderPage()


    @allure.feature("首页头部信息测试")
    @allure.story("点击我的订单")
    @allure.title('test_my_order:我的订单')
    @pytest.mark.run(order=1)
    def test_my_order(self):
        self.header.click_my_order()

    @allure.feature("首页头部信息测试")
    @allure.story("点击会员中心")
    @allure.title('test_vip_center:会员中心')
    @pytest.mark.run(order=2)
    def test_vip_center(self):
        self.header.click_vip_center()

    @allure.feature("首页头部信息测试")
    @allure.story("移动到 关注鲸采电酷")
    @allure.title('test_jingcai_dianku:关注鲸采电酷')
    @pytest.mark.run(order=3)
    def test_jingcai_dianku(self):
        self.header.move_to_jingcaidianku()

    @allure.feature("首页头部信息测试")
    @allure.story("移动到 客户服务")
    @allure.title('test_customer_service:客户服务')
    @pytest.mark.run(order=4)
    def test_customer_service(self):
        self.header.move_to_customer_service()

    @allure.feature("首页头部信息测试")
    @allure.story("点击 商家入驻")
    @allure.title('test_store_settled:商家入驻')
    @pytest.mark.run(order=5)
    def test_store_settled(self):
        self.header.click_store_settled()

    @allure.feature("首页头部信息测试")
    @allure.story("点击 商家登录")
    @allure.title('test_store_login:商家登录')
    @pytest.mark.run(order=6)
    def test_store_login(self):
        self.header.click_store_login()

    @allure.feature("首页头部信息测试")
    @allure.story("点击 联系我们")
    @allure.title('test_contact_us:联系我们')
    @pytest.mark.run(order=7)
    def test_contact_us(self):
        self.header.click_contact_us()

    @allure.feature("首页头部信息测试")
    @allure.story("点击 退出")
    @allure.title('test_exit:退出')
    @pytest.mark.run(order=8)
    def test_exit(self):
        self.header.click_exit()


    def teardown_class(self):
        self.header.web_quit()


if __name__ == '__main__':

    pytest.main(['-vs',"testHeader.py","--alluredir","../report/header_report/allure-result"])
    os.system(r"allure generate --clean ../report/header_report/allure-result -o ../report/header_report/allure-report")