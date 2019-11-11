#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午2:14
# @Author  : yinxin
# @File    : util
# @Software: PyCharm


import base64
from common import api_config
from common import hlog
import requests
import uuid
import re
import os
import json

PLATFORM_MAP = {
    "https://www.zhipin.com": "boss直聘",
    "https://www.51job.com": "前程无忧",
    "https://www.lagou.com": "拉勾",
    "https://www.zhaopin.com": "智联招聘"
}

def send_data(source_url, htmlString):
    if "" == htmlString:
        return
    spider_uuid = uuid.uuid1()

    encodedBytes = base64.b64encode(htmlString.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    data = {
        "url": source_url,
        "spiderUuid": spider_uuid,
        "platform": PLATFORM_MAP[re.match("(http|https)://(www.)?(\w+(\.)?)+",source_url).group()],
        "htmlString": encodedStr
    }

    headers = {
        "content-type": "application/json"
    }

    url = "http://%s:%s%s"%(
        api_config.host,
        api_config.port,
        api_config.uri
    )
    requests.post(url=url, data= data, headers= headers)

def crawl_url(url):

    output = os.popen("node spider.js %s" % url).read()
    jsonString = json.loads(output)
    html = ""
    if "success" == jsonString["code"]:
        html = jsonString["data"]
    else:
        hlog.debug("爬虫爬取有误")

    return html