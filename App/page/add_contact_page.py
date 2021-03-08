#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: add_contact_page.py
@time: 2021/3/8 14:25
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.base_page import BasePage
from App.page.edit_contact_page import EditContactPage


class AddContactPage(BasePage):
    def add_contact_manual(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditContactPage(self.driver)