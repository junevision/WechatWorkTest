#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: app.py
@time: 2021/3/8 14:15
@desc: Activate app, stop app, restart app
"""
import yaml
from appium import webdriver
from App.page.base_page import BasePage
from App.page.main_page import MainPage

with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    IP = datas['server']['IP']
    port = datas['server']['port']


class App(BasePage):
    def start(self):
        if self.driver == None:  # if no driver, initial driver
            self.driver = webdriver.Remote(f"http://{IP}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:  # if driver exists, just launch and reuse the driver
            self.driver.launch_app()
        return self  # use self function

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)