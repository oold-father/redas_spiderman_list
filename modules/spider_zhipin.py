#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午1:57
# @Author  : yinxin
# @File    : spider_zhipin
# @Software: PyCharm

from modules import Spider
from common import hlog
from conf import delay
from utils import crawl_url,send_data
import time

class SpiderZhipin(Spider):

    def __init__(self,url,num):

        self.start_url = url.split("?")[0]
        self.max_page = num

        hlog.var("SpiderZhipin.start_url", self.start_url)
        hlog.var("SpiderZhipin.max_page", self.max_page)

    def handle(self):
        url_list = [self.start_url + "?page=%s&ka=page-%s"%(i,i) for i in range(1,self.max_page+1)]

        for url in url_list:
            html = crawl_url(url)
            send_data(url, html)

        time.sleep(delay)


