#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: personal_info_page.py
@time: 2021/3/10 14:25
@desc: 
"""
from appium.webdriver.common.mobileby import MobileBy
from App.page.base_page import BasePage
from App.page.edit_member_page import EditMemberPage


class PersonalInfoPage(BasePage):
    def goto_edit_member(self):
        # click on more button
        elements = self.finds(MobileBy.XPATH,
                              "//*[@text='个人信息']/../../../../..//*[@class='android.widget.TextView']")
        elements[2].click()
        # click on Edit Member button
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return EditMemberPage(self.driver)
