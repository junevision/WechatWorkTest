#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: search_contact_page.py
@time: 2021/3/10 14:15
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from App.page.base_page import BasePage
from App.page.personal_info_page import PersonalInfoPage


class SearchContactPage(BasePage):
    def search_contact(self, member_name):
        # input target member name on search text
        self.find_and_send_keys(MobileBy.XPATH, "//*[@text='搜索']", member_name)
        # set more implicitly wait for the element
        self.driver.implicitly_wait(20)
        # simulate keyboard Enter
        self.driver.keyevent(66)
        self.driver.press_keycode(66)
        # find_elements return list
        ele_list = self.finds(MobileBy.XPATH, f"//*[@text='{member_name}']")
        if len(ele_list) > 1:
            ele_list[1].click()  # click on the found delete member from list, and go to personal page
        else:
            raise NoSuchElementException(f"cannot found {member_name} on the search list")
        # set back to default setting for implicitly wait
        self.driver.implicitly_wait(5)
        return PersonalInfoPage(self.driver)