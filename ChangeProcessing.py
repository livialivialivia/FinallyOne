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
        driver.get(self.use_url + "/sales/receive")

        driver.find_element_by_link_text(u"确定接单").click()
        sleep(5)

        print u"已经接单"

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
