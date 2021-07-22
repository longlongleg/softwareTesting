#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/17 16:44
# @Author : lumi
# @File : testMine.py
# @Software: PyCharm

import os

import allure
import pytest

from autoStruct.jingcaiAuto.webPage.minePage import MinePage


class TestMine:

    def setup_class(self):
        self.mine = MinePage()

    @allure.feature("我的鲸采电酷")
    @allure.story("点击我的鲸采电酷下面的订单中心")
    @allure.step("登录后，点击我的订单，来到我的鲸采酷站列表，点击订单中心下面的子项目")
    @allure.description("测试点击我的鲸采电酷下面的订单中心")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('item', ['我的咨询', '我的评价', '我的优惠劵'])
    def test_order_center(self, item):
        self.mine.order_center(item)

    @allure.feature("我的鲸采电酷")
    @allure.story("点击我的鲸采电酷下面的我的收藏")
    @allure.step("登录后，点击我的订单，来到我的鲸采酷站列表，点击我的收藏下面的子项目")
    @allure.description("测试点击我的鲸采电酷下面的我的收藏")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('item,expected', [('收藏的商品', '收藏的商品'), ('收藏的店铺', '关注的店铺'), ('我的浏览记录', '浏览记录')])
    def test_my_collection(self, item, expected):
        self.mine.my_collection(item, expected)

    @allure.feature("我的鲸采电酷")
    @allure.story("点击我的鲸采电酷下面的客户服务")
    @allure.step("登录后，点击我的订单，来到我的鲸采酷站列表，点击客户服务下面的子项目")
    @allure.description("测试点击我的鲸采电酷下面的客户服务")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('item,expected',
                             [('我的退货', '退货'), ('我的换货', '换货'), ('提现申请', '提现申请'), ('账户余额', '收支明细'), ('我的投诉', '投诉')])
    def test_my_collection(self, item, expected):
        self.mine.my_collection(item, expected)

    @allure.feature("我的鲸采电酷")
    @allure.story("点击我的鲸采电酷下面的账户中心")
    @allure.step("登录后，点击我的订单，来到我的鲸采酷站列表，点击账户中心下面的子项目")
    @allure.description("测试点击我的鲸采电酷下面的账户中心")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('item,expected',
                             [('会员中心', 'expected address'), ('我的个人资料', 'expected address'), ('我的积分', 'expected address'), ('我的经验值', 'expected address'), ('收货地址', 'expected address')])
    def test_account_center(self, item, expected):
        self.mine.account_center(item, expected)


if __name__ == '__main__':
    pytest.main(['-vs', "testMine.py", "--alluredir", "../report/mine_report/allure-result"])
    os.system(r"allure generate --clean ../report/mine_report/allure-result -o ../report/mine_report/allure-report")
