#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: register_page.py
@time: 2021/3/2 10:39
@desc: This is register page for new users
"""
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("LMJPHOTO_TEST")  # Company Name
        self.driver.find_element(By.XPATH, "//*[@id='manager_name']").send_keys("LMJ_TEST")  # Admin Name
