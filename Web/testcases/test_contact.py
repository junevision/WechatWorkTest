#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_contact.py
@time: 2021/3/2 11:44
@desc: This cases are to test the contact function
"""
from Web.contact_page.main_page import MainPage


class TestContact:
    def test_add_member(self):
        main = MainPage()
        main.goto_contact().add_member()