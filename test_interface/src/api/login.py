from test_interface.src.api.goods import Goods
from test_interface.src.base.baseapi import Base


class Login(Base, ):
    url = ""
    method = ""
    params = {}

    __attrs__ = [

    ]

    def get_goods_list(self):
        self.http_send()
        return self, Goods

    def get_goods_detail(self):
        self.http_send()
        return self, Goods

    class Meta:
        file = ""



