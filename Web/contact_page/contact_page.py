#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: contact_page.py
@time: 2021/3/2 11:43
@desc: This page is contact page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")  # "add members" button
            eles[-1].click()  # click on button
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            # "Save and continue to add" button
            return len(eles) > 0  # check the button exist or not

        WebDriverWait(self.driver, 8).until(wait_name)
        # Enter the name
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("Harry Potter")
        # Enter the Alias
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_english_name']").send_keys("Lovely Harry")
        # Enter account, it is a member's unique identifier cannot be changed once determined
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("Harry001")
        # Enter Mobile phone
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("13800138000")
        # Click on "Save" button
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
