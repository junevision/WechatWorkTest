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

    def __init__(self, driver: WebDriver=None):
        self.driver = driver
        self.logger = self.get_logger("20210310", "../logs")

    def find(self, locator, value):
        self.logger.info("find")
        self.logger.info(f"{locator}, {value}")
        element = self.driver.find_element(locator, value)
        return element

    def finds(self, locator, value):
        self.logger.info("finds")
        self.logger.info(f"{locator}, {value}")
        elements = self.driver.find_elements(locator, value)
        return elements

    def find_and_click(self, locator, value):
        self.logger.info("find and click")
        self.logger.info(f"{locator}, {value}")
        self.find(locator, value).click()

    def find_and_send_keys(self, locator, value, input_keys):
        self.logger.info("find and send keys")
        self.logger.info(f"{locator}, {value}")
        self.find(locator, value).send_keys(input_keys)

    def swipe_find(self, text, nums=3):
        # default set to swipe triple times
        for num in range(nums):
            if num == nums - 1:
                self.logger.info("set implicitly_wait: 5")
                self.driver.implicitly_wait(5)  # set back to caps
                raise NoSuchElementException(f"Have found {nums} times, but not found.")
            self.logger.info("set implicitly_wait: 1")
            self.driver.implicitly_wait(1)  # enhance performance
            try:  # if element displays on current screen, then just return element directly
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)  # set back to caps
                return element
            except:  # if current page is needed to swipe up for more details, then swipe until finding out element
                self.logger.info("not found target element when swiping")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def get_logger(self, logger_name, log_dir):
        log_format = '[%(levelname)s] - %(asctime)s - %(message)s'  # define logging output format
        logger = logging.getLogger(logger_name)  # create logger
        logger.setLevel(logging.DEBUG)  # activate log level
        # verify whether existed logger, in case print logging again
        if not logger.handlers:
            # FileHandler: write into file
            file_handler = logging.FileHandler(log_dir + '/' + 'result_' + logger_name + '.log', encoding='utf-8', mode="a", delay=True)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(logging.Formatter(log_format))
            # StreamHandler: output to console
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            stream_handler.setFormatter(logging.Formatter(log_format))
            # logger to handle FileHandler,StreamHandler
            # output to console and save to file
            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)
        return logger
