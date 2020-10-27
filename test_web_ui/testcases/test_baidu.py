# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 17:30
from time import sleep

import allure
import pytest
from selenium import webdriver


@pytest.mark.parametrize("num", [
    1, 2, 3, 4, 5, 6, 7, 8,
    1, 2, 3, 4, 5, 6, 7, 8,
    1, 2, 3, 4, 5, 6, 7, 8,
])
def test(num):
    caps = {}
    caps.update({"browserName": "chrome"})
    driver = webdriver.Remote("http://192.168.101.38:4444/wd/hub", caps)
    print("打开百度首页")
    driver.get("http://www.baidu.com")
    sleep(5)
    pic = driver.get_screenshot_as_png()
    allure.attach(pic, name="贴图", attachment_type=allure.attachment_type.PNG)
    sleep(10)
    driver.quit()
    print("退出浏览器")
