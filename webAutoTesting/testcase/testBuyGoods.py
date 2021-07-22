#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/19 10:48
# @Author : lumi
# @File : testBuyGoods.py
# @Software: PyCharm
import os

import allure
import pytest

from autoStruct.jingcaiAuto.webPage.buyGoodsPage import BuyGoodsPage


class TestBuyGoods:

    def setup_class(self):
        self.buy = BuyGoodsPage()

    @allure.feature("下单购买商品")
    @allure.story("点击商品进行购买支付")
    @allure.step("登录后，点击首页的某一个商品，然后加入最小数量，点击购买，使用余额进行付款")
    @allure.description("测试商品下单购买付款全流程")
    @pytest.mark.run(order=1)
    #@pytest.mark.skip
    def test_buy_goods(self):
        self.buy.choose_goods('鲸采颈椎按摩器 颈部按摩仪脖子颈肩理疗器揉捏护颈椎仪新品')
        self.buy.add_num()
        self.buy.buy_and_pay()

    @allure.feature("下单购买商品")
    @allure.story("点击商品进行购买，选择收获地址进行支付购买")
    @allure.step("登录后，点击首页的某一个商品，然后加入最小数量，点击购买，修改收货地址，使用余额进行付款")
    @allure.description("测试商品下单购买付款全流程")
    @pytest.mark.run(order=2)
    #@pytest.mark.skip
    def test_buy_goods_changeaddress(self):
        self.buy.choose_goods('可视挖耳勺智能高清带灯发光掏耳朵儿童吸耳屎采耳棒神器')
        self.buy.add_num()
        self.buy.change_address()
        self.buy.buy_and_pay()

    @allure.feature("下单购买商品")
    @allure.story("点击商品，点击预售功能，进行预售商品预定购买")
    @allure.step("登录后，点击首页的某一个商品，然后点击锁定货源，选择样式以及数量，进行购买")
    @allure.description("测试商品下预售单购买付款全流程")
    @pytest.mark.run(order=3)
    def test_buy_presale_goods(self):
        self.buy.choose_goods('鲸采新品夏季手持风扇 小巧便携二合一可折叠无线充风扇挂脖')
        self.buy.presale_btn()
        self.buy.choose_style_counts()
        self.buy.presale_buy_and_pay()



if __name__ == '__main__':
    pytest.main(['-vs', "testBuyGoods.py", "--alluredir", "../report/buyGoods_report/allure-result"])
    os.system(r"allure generate --clean ../report/buyGoods_report/allure-result -o ../report/buyGoods_report/allure-report")

