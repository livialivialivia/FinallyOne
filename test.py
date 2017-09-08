#!/usr/bin/python
# _*_ coding: utf-8 _*_


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select


class ChangeProcessing(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.php.mxj.mx/dev/mock/user/init?mxj_pwd=13880120524&user_type=sales&user_id=34&action=login"
        self.use_url = "http://dev.php.mxj.mx"

    def test_changeprocessing( self ):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "t")
        driver.get(self.use_url + "/sales/my")

        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"排队蓄客")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        driver.find_element_by_xpath("(//input[@type='date'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='date'])[2]").send_keys("2018-09-09")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为排队蓄客"
        sleep(10)
        driver.refresh()
        sleep(5)

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
