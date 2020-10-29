# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/29 17:50
from time import sleep

from selenium.webdriver.common.by import By

from test_web_ui.pageobject.base import BasePage


class Baidu(BasePage):

    _base_url = "http://www.baidu.com"

    def search(self):
        self.find(By.XPATH, '//input[@id="kw"]', "输入搜索词").send_keys("python")
        sleep(2)
