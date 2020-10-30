# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/29 16:50
import pytest

from test_web_ui.pageobject.baidu import Baidu


class TestBase:

    def setup(self):
        self.ts = Baidu()

    def teardown(self):
        self.ts.close()


    @pytest.mark.parametrize("num", [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
        11, 21, 31, 41, 51, 61, 71, 81, 91, 12,
        13, 23, 33, 43, 53, 63, 73, 83, 93, 45,
        13, 23, 33, 43, 53, 63, 73, 83, 93, 45,
    ])
    def test_01(self, num):
        self.ts.search()

