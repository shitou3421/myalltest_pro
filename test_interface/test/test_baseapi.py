import pytest

from test_interface.src.api.login import Login


class Test:

    def setup(self):
        self.req = Login()
        self.Meta = self.req.Meta

    def teardown(self):
        pass

    @pytest.mark.parametrize()
    def test_sendapi(self):
        self.req.get_goods_list()[1].chenge_goods_info()
        self.req.get_goods_list()[0].get_goods_list()
        assert '200' == self.req.resp










