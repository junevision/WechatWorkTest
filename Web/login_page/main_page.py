#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: main_page.py
@time: 2021/3/2 10:38
@desc: This is the main page without login in
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.login_page.login_page import LoginPage
from Web.login_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(6)

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()  # Sign Up button
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()  # Login button
        return LoginPage(self.driver)