#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: address_list_page.py
@time: 2021/3/8 14:22
@desc: 
"""
from App.page.add_contact_page import AddContactPage
from App.page.base_page import BasePage


class AddressListPage(BasePage):
    def click_add_contact(self):
        self.swipe_find("添加成员").click()
        return AddContactPage(self.driver)