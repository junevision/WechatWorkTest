#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: login_page.py
@time: 2021/3/2 10:39
@desc: This is the login page, including scan QR code and Company registration
"""
from selenium.webdriver.common.by import By
from Web.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()  # Company registration
        return RegisterPage(self.driver)