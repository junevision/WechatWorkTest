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
from selenium.common.exceptions import NoSuchElementException


class TestWeWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["automationName"] = "uiautomator2"  # activate toast verify
        caps["noReset"] = "true"
        caps["skipServerInstallation"] = "true"  # skip uiautomator2 server installation
        caps["skipDeviceInitialization"] = "true"  # skip device initialization
        caps['unicodeKeyboard'] = 'true'
        caps['resetKeyboard'] = 'true'
        caps["dontStopAppOnReset"] = "true"  # don't stop app on reset, but here need to start from launch page
        # caps['settings[waitForIdleTimeout]'] = 1  # set the wait time for dynamic page, this is for dynamic punch time
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
                                 '.text("打卡").instance(0));').click()  # android only, uiautomator2 scroll function
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)  # print the whole page source
        # activate implicitly wait via find element
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        assert "外出打卡成功" in self.driver.page_source

    def swipe_find(self, text, nums=3):
        # default set to swipe triple times
        for num in range(nums):
            if num == nums - 1:
                self.driver.implicitly_wait(5)  # set back to caps
                raise NoSuchElementException(f"Have found {nums} times, but not found.")

            self.driver.implicitly_wait(1)  # enhance performance
            try:  # if element displays on current screen, then just return element directly
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)  # set back to caps
                return element
            except:  # if current page is needed to swipe up for more details, then swipe until finding out element
                print("not found")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.2

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def test_add_member(self):
        """
        precondition: signed in statement(noReset=True)
        add member in enterprise testcases:
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、点击【添加成员】
        4、点击【手动输入添加】
        5、输入【姓名手机号】
        6、点击【保存】
        7、验证【添加成功】
        8、退出【企业微信】应用
        """
        member_name = "test006"
        mobile_number = "13800000001"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.swipe_find("添加成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(member_name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(mobile_number)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")  # assert toast

    def test_delete_member(self):
        """
        precondition: signed in statement(noReset=True)
        add member in enterprise testcases:
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、点击【查询】
        4、输入【要删除的成员名字】
        5、点击【搜索出来的结果】
        6、点击右上角【更多按钮】
        7、点击【编辑成员】
        8、点击【删除成员】
        9、点击【确定】
        10、验证【无搜索结果】
        11、退出【企业微信】应用
        """
        delete_member = "test006"
        # go to address list page
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # contact page
        # click search button
        eles = self.driver.find_elements(MobileBy.XPATH,
                                         "//*[@text='我的客户']/../../..//*[@class='android.widget.TextView']")
        eles[1].click()
        # go to search contact page
        # input delete member name on search text
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys(delete_member)
        # set more implicitly wait for the element
        self.driver.implicitly_wait(10)
        # simulate keyboard Enter
        self.driver.keyevent(66)
        self.driver.press_keycode(66)
        # find_elements return list
        ele_list = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{delete_member}']")
        if len(ele_list) > 1:
            ele_list[1].click()  # click on the found delete member from list, and go to personal page
        else:
            raise NoSuchElementException(f"cannot found {delete_member} on the search list")
        # set back to default setting for implicitly wait
        self.driver.implicitly_wait(5)
        # personal info page
        # click on more button
        elements = self.driver.find_elements(MobileBy.XPATH,
                                             "//*[@text='个人信息']/../../../../..//*[@class='android.widget.TextView']")
        elements[2].click()
        # click on Edit Member button
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # go to Edit Member page
        # click on delete member button
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # click on confirm yes button
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        # assert no result
        self.driver.find_element(MobileBy.XPATH, "//*[@text='无搜索结果']")
