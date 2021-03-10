#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: address_list_page.py
@time: 2021/3/8 14:22
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.add_contact_page import AddContactPage
from App.page.base_page import BasePage
from App.page.search_contact_page import SearchContactPage


class AddressListPage(BasePage):
    def click_add_contact(self):
        self.swipe_find("添加成员").click()
        return AddContactPage(self.driver)

    def click_search_contact(self):
        eles = self.finds(MobileBy.XPATH,
                          "//*[@text='我的客户']/../../..//*[@class='android.widget.TextView']")
        eles[1].click()
        return SearchContactPage(self.driver)
