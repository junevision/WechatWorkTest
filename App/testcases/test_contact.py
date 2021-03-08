#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_contact.py
@time: 2021/3/8 14:36
@desc: 
"""
from App.page.app import App


class TestContact:

    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_add_contact(self):
        member_name = "test009"
        mobile_number = "13800000004"
        edit_page = self.main.goto_address_list().click_add_contact().add_contact_manual()
        edit_page.edit_contact(member_name, mobile_number)
        edit_page.verify_okay()
