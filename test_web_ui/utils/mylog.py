# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 10:45
import logging
import os
import sys
import time
from logging import handlers

from test_web_ui.utils.utils import Utils


class Logger:
    logfile_dir = os.path.join(Utils.get_proj_path(), "log")
    logfile_name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + ".log"
    logfile_path = os.path.join(logfile_dir, logfile_name)

    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL,
    }

    def __init__(self, level='debug', when='D', backCount=3, fmt='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(self.logfile_path)
        self.logger.handlers = []
        format_str = logging.Formatter(fmt=fmt)
        self.logger.setLevel(self.level_relations.get(level))
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(format_str)
        time_handler = handlers.TimedRotatingFileHandler(filename=self.logfile_path, when=when, backupCount=backCount, encoding='utf-8')
        time_handler.setFormatter(format_str)
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(time_handler)


log = Logger().logger

if __name__ == '__main__':
    print(Logger.logfile_path)
