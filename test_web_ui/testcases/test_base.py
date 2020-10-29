# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/29 16:50
import pytest

from test_web_ui.pageobject.baidu import Baidu


class TestBase:

    def setup(self):
        self.ts = Baidu()

    @pytest.mark.parametrize("num", [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
    ])
    def test_01(self, num):
        self.ts.search()
