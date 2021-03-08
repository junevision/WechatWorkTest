#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: main_page.py
@time: 2021/3/8 14:19
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.address_list_page import AddressListPage
from App.page.base_page import BasePage


class MainPage(BasePage):

    address_list_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_address_list(self):
        # click contact tab
        self.find_and_click(*self.address_list_element)
        return AddressListPage(self.driver)