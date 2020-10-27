# -*- coding:utf-8 -*-
# author:shitou
# datetime:2020/10/27 9:46
import os

import allure
from appium import webdriver as a_webdriver
from selenium import webdriver as s_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_web_ui.utils.mydecorator import rerun_failer_step
from test_web_ui.utils.mylog import Logger
from test_web_ui.utils.utils import Utils



class BasePage:

    log = Logger().logger

    def __init__(self, driver: WebDriver, headless=False):
        '''
        根据设置的环境变量，判断实例化selenium的driver还是appium的driver
        环境变量参数设置为：
            - runtype： web / mobile
            - browser： 当runtype为web时生效，可接受参数chrome / ie / edge / firefox
        '''
        run_type = os.getenv("runtype", default="web")
        browser = os.getenv("browser", default="chrome")

        if run_type == "web":
            if driver:
                self.driver = driver
            else:
                if browser.lower() == "chrome":
                    options = s_webdriver.ChromeOptions()
                    if headless:
                        options.add_argument("--headless")
                        options.add_argument("window-size=1920×3000")
                        options.add_argument("--disable-gpu")
                    self.driver = s_webdriver.Chrome(options=options)
                elif browser.lower() == "ie":
                    self.driver = s_webdriver.Ie()
                elif browser.lower() == "edge":
                    self.driver = s_webdriver.Edge()
                elif browser.lower() == "firefox":
                    self.driver = s_webdriver.Firefox()
                else:
                    raise Exception("传入不支持的浏览器，请修改！！！")
        elif run_type == "mobile":
            caps = {}
            path = os.path.join(Utils.get_proj_path(), "config", "appium_config.yml")
            raw_data = Utils.read_yaml(path=path)
            host = raw_data.get("host")
            port = raw_data.get("port")
            dic_data = raw_data.get("caps")
            appPackage = ""
            appActivity = ""

            for k, v in dic_data.items():
                if k == "appPackage":
                    appPackage = v
                if k == "appActivity":
                    appActivity = v

            if driver is None:
                for data in dic_data:
                    caps.update(data)
                self.log.info("启动参数为：host - [{host}], port - [{port}], caps - [{caps}]".format(host=host, port=port, caps=caps))
                try:
                    self.driver = a_webdriver.Remote("http://{host}:{port}/wd/hub".format(host=host, port=port), caps)
                    self.driver.implicitly_wait(5)
                except:
                    raise RuntimeError("初始化driver出错，请检查")

            else:
                try:
                    self.driver.start_activity(appPackage, appActivity)
                except:
                    raise RuntimeError("跳转主页出错，请检查")
        else:
            raise Exception("传入不支持的设备类型，请修改！！！")

    @rerun_failer_step
    def find(self, locator, value=None, massage=None):
        '''
        支持传递的定位方式有：
        1、 find((By.XPATH, "//*[@class='xxx']"， "点击登录按钮")) -- 推荐
        2、 find((By.XPATH, "//*[@class='xxx']"))
        3、 find(By.XPATH, value="//*[@class='xxx']", massage="点击登录按钮")
        4、 find(By.XPATH, value="//*[@class='xxx']")
        :param locator:
        :param value:
        :param massage:
        :return: element
        '''
        self.log.info(f"当前查找find传入参数：[{locator}] - [{value}] - [{massage}]")
        if isinstance(locator, tuple):
            try:
                by, val, msg = locator
                self.wait(by, val)
                element = self.driver.find_element(by=by, value=val)
                pic = self.driver.get_screenshot_as_png()
                allure.attach(pic, name=msg, attachment_type=allure.attachment_type.PNG)
            except ValueError:
                by, val = locator
                self.wait(by, val)
                element = self.driver.find_element(by=by, value=val)
                pic = self.driver.get_screenshot_as_png()
                allure.attach(pic, name=val, attachment_type=allure.attachment_type.PNG)
        else:
            self.wait(locator, value)
            element = self.driver.find_element(by=locator, value=value)
            pic = self.driver.get_screenshot_as_png()
            if massage:
                allure.attach(pic, name=massage, attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach(pic, name=value, attachment_type=allure.attachment_type.PNG)
        return element

    @rerun_failer_step
    def finds(self, locator, value=None, massage=None):
        '''
        支持传递的定位方式有：
        1、 finds((By.XPATH, "//*[@class='xxx']"， "点击登录按钮")) -- 推荐
        2、 finds((By.XPATH, "//*[@class='xxx']"))
        3、 finds(By.XPATH, value="//*[@class='xxx']", massage="点击登录按钮")
        4、 finds(By.XPATH, value="//*[@class='xxx']")
        :param locator:
        :param value:
        :param massage:
        :return: elements
        '''
        self.log.info(f"当前查找finds传入参数：[{locator}] - [{value}] - [{massage}]")
        if isinstance(locator, tuple):
            try:
                by, val, msg = locator
                self.wait(by, val)
                elements = self.driver.find_elements(by=by, value=val)
                pic = self.driver.get_screenshot_as_png()
                allure.attach(pic, name=msg, attachment_type=allure.attachment_type.PNG)
            except ValueError:
                by, val = locator
                self.wait(by, val)
                elements = self.driver.find_elements(by=by, value=val)
                pic = self.driver.get_screenshot_as_png()
                allure.attach(pic, name=val, attachment_type=allure.attachment_type.PNG)
        else:
            self.wait(locator, value)
            elements = self.driver.find_elements(by=locator, value=value)
            pic = self.driver.get_screenshot_as_png()
            if massage:
                allure.attach(pic, name=massage, attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach(pic, name=value, attachment_type=allure.attachment_type.PNG)
        return elements


    def wait(self, locator, value=None, time=10):
        '''显示等待元素可点击'''
        if isinstance(locator, tuple):
            WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))
        else:
            WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable((locator, value)))

    def find_by_text(self, xpath):
        element = self.find(By.XPATH, xpath)
        return element

    def finds_by_text(self, xpath):
        elements = self.finds(By.XPATH, xpath)
        return elements














