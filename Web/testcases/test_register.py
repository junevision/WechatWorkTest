#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_register.py
@time: 2021/3/2 11:19
@desc: This cases are testing the register logic from different entrances
"""
from time import sleep
from Web.login_page.main_page import MainPage


class TestRegister:
    def test_register(self):
        main = MainPage()
        main.goto_register().register()
        sleep(2)

    def test_login_register(self):
        main = MainPage()
        main.goto_login().goto_register().register()
        sleep(2)