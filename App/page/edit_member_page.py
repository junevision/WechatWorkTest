#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: edit_member_page.py
@time: 2021/3/10 14:31
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.base_page import BasePage


class EditMemberPage(BasePage):
    def delete_member(self):
        # click on delete member button
        self.find_and_click(MobileBy.XPATH, "//*[@text='删除成员']")
        # click on confirm yes button
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")

    def verify_okay(self):
        # assert no result
        self.find(MobileBy.XPATH, "//*[@text='无搜索结果']")