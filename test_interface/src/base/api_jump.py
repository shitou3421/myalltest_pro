class ApiJump:
    '''
    该类用于提供api跳转过程中的返回值的封装
    原始：
    def get_goods_list(self):
        self.http_send()
        return self, Goods
    调用：
    self.req.get_goods_list()[1].chenge_goods_info()
    self.req.get_goods_list()[0].get_goods_list()

    封装后：
    def get_goods_list(self):
        self.http_send()
        return ApiJump
    调用：
    self.req.get_goods_list().get_goods_list()

    '''

    def ret(self):
        pass

    def __getattribute__(self, item):
        pass
