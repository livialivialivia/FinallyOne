#!/usr/bin/python
# _*_ coding: utf-8 _*_

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class ChangeStatus(unittest.TestCase):
    def setUp( self ):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://dev.php.mxj.mx/dev/mock/user/init?mxj_pwd=13880120524&user_type=sales&user_id=34&action=login"
        self.use_url = "http://dev.php.mxj.mx"



    def test_changestatus( self ):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + "t")
        driver.get(self.use_url + "/sales/my")
        driver.maximize_window()

        #电话邀约
        sleep(3)
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"电话邀约")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为电话邀约"
        sleep(10)

        #等待参观
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"等待参观")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为等待参观"
        sleep(10)

        #需求沟通
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"需求沟通")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(u"公司名称填写")
        driver.find_element_by_xpath("(//input[@type='date'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='date'])[2]").send_keys("2018-09-09")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为需求沟通"
        sleep(10)

        # 方案报价
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"方案报价")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为方案报价"
        sleep(10)

        # 输单
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"输单")
        sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[1]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[1]").send_keys(u"工位输单原因")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"企业会员输单原因")
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(u"个人会员输单原因")
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(u"活动场地输单原因")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为输单"
        sleep(10)

        #重新打开线索
        driver.find_element_by_xpath("//div[3]").click()
        driver.find_element_by_link_text(u"重新打开").click()
        sleep(5)
        driver.find_element_by_css_selector("div.app-container > div.weui_dialog_confirm > div.weui_dialog > div.weui_dialog_ft > a.weui_btn_dialog.primary").click()
        sleep(5)
        driver.refresh()
        print u"线索已经重新打开"

        #修改为无效单
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"无效单")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为无效单"
        sleep(10)

        #重新打开
        driver.find_element_by_xpath("//div[3]").click()
        driver.find_element_by_link_text(u"重新打开").click()
        sleep(5)
        driver.find_element_by_css_selector("div.app-container > div.weui_dialog_confirm > div.weui_dialog > div.weui_dialog_ft > a.weui_btn_dialog.primary").click()
        sleep(5)
        driver.refresh()
        print u"线索已经重新打开"

        #修改为排队蓄客
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"排队蓄客")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为排队蓄客"
        sleep(10)

        #重新打开
        driver.find_element_by_xpath("//div[3]").click()
        driver.find_element_by_link_text(u"重新打开").click()
        sleep(5)
        driver.find_element_by_css_selector("div.app-container > div.weui_dialog_confirm > div.weui_dialog > div.weui_dialog_ft > a.weui_btn_dialog.primary").click()
        sleep(5)
        driver.refresh()
        print u"线索已经重新打开"

        #修改为签单完成
        driver.find_element_by_link_text(u"下一步").click()
        sleep(3)
        Select(driver.find_element_by_css_selector("select.weui_select")).select_by_visible_text(u"签单完成")
        driver.find_element_by_xpath("(//input[@type='text'])[1]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[1]").send_keys("bj-jtdx-20160521-234651")
        sleep(3)
        Select(driver.find_element_by_css_selector("select.tOrderComment-dateSelect.tOrderComment-input")).select_by_visible_text("09:00")
        driver.find_element_by_css_selector("textarea.weui_textarea").clear()
        driver.find_element_by_css_selector("textarea.weui_textarea").send_keys(u"详细说明")
        sleep(3)
        driver.find_element_by_link_text(u"确定").click()
        sleep(3)
        driver.find_element_by_css_selector("a.weui_btn_dialog.primary").click()
        print u"线索状态切换为签单完成"
        sleep(10)

    def tearDown( self ):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
