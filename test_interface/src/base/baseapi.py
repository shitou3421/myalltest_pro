import json

import requests


class Base:
    '''
    提供发送请求的能力
    '''

    params = {}  # 单个请求的特定参数

    resp: requests.Response.text = None

    def __init__(self):
        self.base_config = []
        self._session = requests.Session()
        self.common_params = None  # 所有请求的公共参数
        self.common_headers = None


    def http_send(self, data: dict):
        '''
        发送http请求
        :param response_type: 响应体的格式，默认使用restfull风格的json
        :return:
        '''
        response_type = data.get("response_type")
        method = data.get("method")
        url = data.get("url")
        param = data.get("params")

        raw_params = json.dumps(param)
        for key, value in self.params.items():
            params_ = raw_params.replace(f"${{{key}}}", value)
        params = json.loads(params_)

        self._session.params.update(self.common_params)
        self._session.headers.update(self.common_headers)
        self.r = self._session.request(method=method, url=url, params=params)

        if "json" == response_type:
            self.resp = self.r.json()
        else:
            self.resp = self.r.text

        return self.resp

