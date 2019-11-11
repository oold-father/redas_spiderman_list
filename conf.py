#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 上午10:28
# @Author  : yinxin
# @File    : congig
# @Software: PyCharm

from modules import SpiderZhipin, SpiderLagou


# 网页域名到网站名字的映射
PLATFORM_MAP = {
    "zhipin": "boss直聘",
    "51job": "前程无忧",
    "lagou": "拉勾",
    "zhaopin": "智联招聘"
}

# 域名主体和对应的爬虫之间的映射
PLATFORM_SPIDER_MAP = {
    "zhipin": SpiderZhipin,
    "lagou": SpiderLagou
}

# 爬取网页的间隔时间
delay = 3