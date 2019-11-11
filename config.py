#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 上午10:28
# @Author  : yinxin
# @File    : congig
# @Software: PyCharm


from happy_python import HappyConfigBase

class ApiConfig(HappyConfigBase):
    """
    配置文件模板
    """
    def __init__(self):
        super().__init__()

        self.section = "redas_spider_man"
        self.source_host = "127.0.0.1"
        self.source_port = 80
        self.source_url = ""
        self.target_host = "127.0.0.1"
        self.target_port = 80
        self.target_uri = ""