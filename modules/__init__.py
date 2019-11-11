#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午1:52
# @Author  : yinxin
# @File    : __init__.py
# @Software: PyCharm

from modules.spider import Spider
from modules.spider_zhipin import SpiderZhipin
from modules.spider_lagou import SpiderLagou

__all__ = [
    "Spider",
    "SpiderZhipin",
    "SpiderLagou"
]