#!/usr/bin/python
# _*_ coding: utf-8 _*_


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



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

        driver.find_element_by_xpath("//div[3]").click()
        driver.find_element_by_link_text(u"重新打开").click()
        sleep(5)
        driver.find_element_by_css_selector("div.app-container > div.weui_dialog_confirm > div.weui_dialog > div.weui_dialog_ft > a.weui_btn_dialog.primary").click()
        sleep(5)
        driver.refresh()
        print u"线索已经重新打开"

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
