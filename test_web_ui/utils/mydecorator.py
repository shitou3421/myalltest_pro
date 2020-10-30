# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 12:19
from selenium.webdriver.remote.webelement import WebElement

from .mylog import log

def rerun_failer_step(func):
    '''
    用于定位步骤的失败重试
    '''
    rang_times = 4
    def wapper(*args, **kwargs):
        for i in range(rang_times):
            try:
                log.info(f"第 {i} 次调用{func}")
                element = func(*args, **kwargs)
                if isinstance(element, WebElement):
                    return element
            except:
                # todo: 异常的处理，弹窗，广告之类
                continue
        else:
            raise RuntimeError(f"定位 {rang_times} 次未找到，请检查！！！")
    return wapper




