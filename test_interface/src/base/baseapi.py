import requests


class Base:
    '''
    提供发送请求的能力
    '''

    method = None
    url = None
    params = None

    resp: requests.Response.text = None

    def __init__(self):
        self.base_config = []
        self.req = requests.Session()

    def http_send(self, response_type="json"):
        '''
        发送http请求
        :param response_type: 响应体的格式，默认使用restfull风格的json
        :return:
        '''
        self.req.params.update(self.params)
        self.req.headers.update(self.params)
        self.r = self.req.request(method=self.method, url=self.url, params=self.params)
        if "json" == response_type:
            self.resp = self.r.json()
        else:
            self.resp = self.r.text
        return self.resp

