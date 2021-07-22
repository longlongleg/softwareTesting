#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/13 18:20
# @Author : lumi
# @File : testLogin.py
# @Software: PyCharm
import os
import time

import pytest
import allure
from selenium.webdriver.common.by import By

from autoStruct.jingcaiAuto.webPage.loginPage import LoginPage

class TestLogin:

    def setup_class(self):
        self.driver = LoginPage()

    @allure.story("测试买家端登录页面")
    @allure.step("测试用户名不存在情况")
    @allure.title("用户名不存在")
    @pytest.mark.run(order=1)
    def test_login_account_error(self):
        self.driver.send_account('account')
        self.driver.send_password('pwd')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message')) == "用户名或密码错误！"
        self.driver.is_click(*(By.ID,'popup_ok'))
        time.sleep(1)


    @allure.story("测试买家端登录页面")
    @allure.step("测试未输入验证码情况")
    @allure.title("验证码未输入")
    @pytest.mark.run(order=2)
    def test_login_code_blank(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_account('account')
        self.driver.send_password('pwd')
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message')) == "请输入图形验证码"
        self.driver.is_click(*(By.ID, 'popup_ok'))
        time.sleep(1)

    @allure.story("测试买家端登录页面")
    @allure.step("测试密码错误情况")
    @allure.title("密码输入错误")
    @pytest.mark.run(order=3)
    def test_login_password_error(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_account('account')
        self.driver.send_password('pwd')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message')) == "用户名或密码错误！"
        self.driver.is_click(*(By.ID, 'popup_ok'))
        time.sleep(1)

    @allure.story("测试买家端登录页面")
    @allure.step("用户名为空情况")
    @allure.title("用户名未输入")
    @pytest.mark.run(order=4)
    def test_login_account_blank(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_password('pwd')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message')) == "用户名不能为空"
        self.driver.is_click(*(By.ID, 'popup_ok'))
        time.sleep(1)

    @allure.story("测试买家端登录页面")
    @allure.step("密码为空情况")
    @allure.title("密码未输入")
    @pytest.mark.run(order=5)
    def test_login_password_blank(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_account('account')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message'))== "密码不能为空"
        self.driver.is_click(*(By.ID, 'popup_ok'))
        time.sleep(1)

    @allure.story("测试买家端登录页面")
    @allure.step("密码为空情况")
    @allure.title("密码未输入")
    @pytest.mark.run(order=5)
    def test_login_password_blank(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_account('account')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.ele_text(*(By.ID, 'popup_message')) == "密码不能为空"
        self.driver.is_click(*(By.ID, 'popup_ok'))
        time.sleep(1)

    @allure.story("测试买家登录页面的忘记密码链接")
    @allure.step("点击忘记密码链接")
    @allure.title("忘记密码功能")
    @pytest.mark.run(order=6)
    def test_forget_password(self):
        self.driver.forget_password()
        assert self.driver.get_current_url() == 'expected address'
        self.driver.web_back()
        time.sleep(3)

    @allure.story("测试买家登录页面的立即注册链接")
    @allure.step("点击立即注册链接")
    @allure.title("立即注册功能")
    @pytest.mark.run(order=7)
    def test_register_rightly(self):
        self.driver.register_right_now()
        assert self.driver.get_current_url() == 'expected address'
        self.driver.web_back()
        time.sleep(3)

    @allure.story("测试买家端登录页面")
    @allure.step("密码用户名都正确情况")
    @allure.title("密码用户名正确")
    @pytest.mark.run(order=8)
    def test_login_account_ok(self):
        self.driver.account_clear()
        self.driver.password_clear()
        self.driver.code_clear()
        self.driver.send_account('account')
        self.driver.send_password('pwd')
        self.driver.send_code()
        time.sleep(5)
        self.driver.btn_click()
        time.sleep(1)
        assert self.driver.get_current_url() == 'expected address'

    def teardown_class(self):
        time.sleep(3)
        self.driver.web_quit()


if __name__ == '__main__':
    #pytest.main(['-vs','testLogin.py','--html=../report/login_report/login_report.html','--alluredir=../report/login_report/allure-result'])
    #os.system('allure generate ../report/login_report/allure-result -o ../report/login_report/login_report.html --clean')
    pytest.main(['-vs','testLogin.py', '--html=../report/login_report/login_report.html', '--self-contained-html'])





