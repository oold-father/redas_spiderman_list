#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午3:58
# @Author  : yinxin
# @File    : spider_lagou
# @Software: PyCharm

from modules import Spider
from common import hlog, delay
from utils import crawl_url,send_data
import time

class SpiderLagou(Spider):

    def __init__(self,url,num):

        self.primeval_url = url
        self.start_url = url.split("?")[0]
        self.max_page = num
        self.platform = "boss直聘"

        hlog.var("SpiderLagou.primeval_url", self.primeval_url)
        hlog.var("SpiderLagou.start_url", self.start_url)
        hlog.var("SpiderLagou.max_page", self.max_page)
        hlog.var("SpiderLagou.platform", self.platform)

    def handle(self):
        url_list = [self.start_url + "%s/"%(i) for i in range(1,self.max_page+1)]

        for url in url_list:
            html = crawl_url(url)
            send_data(self.primeval_url, html, self.platform)

        time.sleep(delay)