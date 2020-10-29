# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 10:09
import os

import yaml


class Utils:

    @classmethod
    def get_proj_path(cls):
        pro_path = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
        return pro_path


    @classmethod
    def read_yaml(cls, path):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data


if __name__ == '__main__':
    print(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "appium_config.yml")).get("caps"))
    for info in Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "appium_config.yml")).get("caps"):
        for k, v in info.items():
            if k == "appPackage":
                print(k, v)
    print(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "selenium_config.yml")).get("caps"))
    print(type(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "selenium_config.yml")).get("caps")))
    print(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "selenium_config.yml")).get("host"))
    print(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "selenium_config.yml")).get("port"))
    print(Utils.read_yaml(os.path.join(Utils.get_proj_path(), "config", "selenium_config.yml")).get("headless"))






