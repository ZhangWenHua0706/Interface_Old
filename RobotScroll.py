# -*- coding: UTF-8 -*-
from selenium import webdriver
import os
class RobotScroll():
    def __init__(self):
        pass
    def RobotScrollElement(self,param):
        IEdriver="C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = IEdriver
        browser = webdriver.Ie(IEdriver)
        browser.get("http://www.baidu.com")
        browser.find_element_by_id("kw").send_keys('山野村夫'.decode('utf-8'))
        browser.find_element_by_xpath("//*[@id='su']").click()
#       browser.find_element_by_id("su").click()
        target=browser.find_element_by_xpath(param)
        browser.execute_script("arguments[0].scrollIntoView();", target)
        target.click()

if __name__=='__main__':
    rs = RobotScroll()
    rs.RobotScrollElement("//*[@id='s_tab']/a[2]")




