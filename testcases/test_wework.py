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
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWeWork:

    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_register(self):
        """
        Sign in from homepage of WechatWork
        """
        self.driver.get("https://work.weixin.qq.com/")  # original website
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()  # click on login
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()  # Company registration
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("test")  # company name
        sleep(2)

    @pytest.mark.skip
    def test_login_with_debugger(self):
        """
        Reusing chrome browser by port
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # website with login user
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()  # change to contact tab
        self.driver.find_element(By.XPATH, "//*[@id='menu_apps']").click()  # change to app management tab
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_manageTools']").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_profile']").click()

    # @pytest.mark.skip
    def test_login_with_cookies(self):
        """
        Access to website with cookies
        """
        # store cookie, login status first with debugger
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("temp.txt", "w", encoding="utf-8") as f:
        #     json.dump(cookies, f)

        # read cookie, could use general chromedriver
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("temp.txt", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        print(cookies)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(2)
