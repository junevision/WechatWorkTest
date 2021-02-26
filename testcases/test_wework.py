#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_wework.py
@time: 2021/2/26 16:07
@desc: 
"""
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeWork:

    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.vars = {}

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        """
        Sign in from homepage of WechatWork
        """
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("test")
        sleep(6)
        self.driver.close()

    def test_login_tmp(self):
        """
        Reusing chrome browser by port
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_cookie_login(self):
        """
        Access to website with cookies
        """
        # store cookie
        # cookies = self.driver.get_cookies()
        # with open("tmp2.text","w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # read cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp2.text", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)
