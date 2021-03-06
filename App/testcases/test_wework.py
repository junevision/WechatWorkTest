#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mingjun Lei
@file: test_wework.py
@time: 2021/3/6 10:26
@desc: This py file is to test the main function of wechat work APP
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestWeWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["automationName"] = "uiautomator2"  # activate toast verify
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1  # set the wait time for dynamic page
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_punch(self):
        """
        precondition: Signed in statement(noReset=True)
        punch in and out testcases：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        """
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)
        # activate implicitly wait via find element
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        assert "外出打卡成功" in self.driver.page_source

    def test_add_member(self):
        """
        precondition: signed in statement(noReset=True)
        add member in enterprise testcases:
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、点击【添加成员】
        4、点击【手动输入添加】
        5、输入【姓名手机号公司地址】
        6、点击【保存】
        7、验证【添加成功】
        7、退出【企业微信】应用
        """
        member_name = "test005"
        mobile_number = "13800138004"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='必填']").send_keys(member_name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(mobile_number)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='选填' and @class='android.widget.TextView']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='请输入公司地址，例如“腾讯大厦”']").send_keys("腾讯大厦")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']").click()  # don't send invitation
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        toast_element = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        assert "添加成功" == toast_element.text
        back_locator = (MobileBy.ID, "com.tencent.wework:id/gu_")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(back_locator))
        self.driver.find_element(*back_locator).click()  # click back button
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']")
        assert member_name in self.driver.page_source


