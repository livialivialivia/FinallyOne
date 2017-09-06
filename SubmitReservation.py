#!/usr/bin/python
# _*_ coding: utf-8 _*_

# 带看端提交工位线索

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class SubmitReservation(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.php.mxj.mx/dev/mock/user/init?mxj_pwd=13880120524&user_type=sales&user_id=34&action=login"
        self.use_url = "http://dev.php.mxj.mx"



    def test_submitreservation( self ):
        driver = self.driver
        driver.get(self.base_url)
        sleep(10)
        driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "t")
        driver.get(self.use_url + "/sales/recommendation")

        driver.find_element_by_css_selector("input.weui_input").clear()
        driver.find_element_by_css_selector("input.weui_input").send_keys(u"livia测试1")
        driver.find_element_by_xpath("//input[@type='tel']").clear()
        driver.find_element_by_xpath("//input[@type='tel']").send_keys("18782902669")
        driver.find_element_by_css_selector("input.weui_switch").click()
        driver.find_element_by_link_text(u"确定").click()
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()

        print u"工位线索创建成功"
        sleep(10)



    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
