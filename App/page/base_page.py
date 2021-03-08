#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: base_page.py
@time: 2021/3/8 14:43
@desc: 
"""
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


# base class, init driver, find, finds, find and click, find and send keys, swipe_find
class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, locator, value):
        logging.info("find")
        logging.info(locator, value)
        self.driver.find_element(locator, value)

    def finds(self, locator, value):
        logging.info("finds")
        logging.info(locator, value)
        self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        logging.info("find and click")
        logging.info(locator, value)
        self.driver.find_element(locator, value).click()

    def find_and_send_keys(self, locator, value, input_keys):
        logging.info("find and send keys")
        logging.info(locator, value, input_keys)
        self.driver.find_element(locator, value).send_keys(input_keys)

    def swipe_find(self, text, nums=3):
        # default set to swipe triple times
        for num in range(nums):
            if num == nums - 1:
                logging.info("set implicitly_wait: 5")
                self.driver.implicitly_wait(5)  # set back to caps
                raise NoSuchElementException(f"Have found {nums} times, but not found.")
            logging.info("set implicitly_wait: 1")
            self.driver.implicitly_wait(1)  # enhance performance
            try:  # if element displays on current screen, then just return element directly
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)  # set back to caps
                return element
            except:  # if current page is needed to swipe up for more details, then swipe until finding out element
                logging.info("not found")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)