#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: edit_contact_page.py
@time: 2021/3/8 14:26
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.base_page import BasePage


class EditContactPage(BasePage):
    def edit_contact(self, member_name, mobile_number):
        self.find_and_send_keys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']", member_name)
        self.find_and_send_keys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']", mobile_number)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

    def verify_okay(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")