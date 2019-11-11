#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午2:14
# @Author  : yinxin
# @File    : util
# @Software: PyCharm

import inspect
import base64
from common import api_config
from common import hlog
from common import PLATFORM_MAP
import requests
import uuid
import os
import json


def send_data(source_url, htmlString):
    """
    :param source_url: 爬取的是哪个网址
    :param htmlString: 爬取结果的字符串
    :return:
    """
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    hlog.var("source_url", source_url)

    if "" == htmlString:
        hlog.exit_func(func_name)
        return

    spider_uuid = uuid.uuid1()
    hlog.var("spider_uuid", spider_uuid)

    encodedBytes = base64.b64encode(htmlString.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    data = {
        "url": source_url,
        "spiderUuid": spider_uuid,
        "platform": PLATFORM_MAP[get_platfrom(source_url)],
        "htmlString": encodedStr
    }

    headers = {
        "content-type": "application/json"
    }

    url = "http://%s:%s%s"%(
        api_config.target_host,
        api_config.target_port,
        api_config.target_uri
    )

    response = requests.post(url=url, data= data, headers= headers)
    hlog.info("发送结果完成，返回状态%s"%response.status_code)

    hlog.exit_func(func_name)

def crawl_url(url):
    """
    :param url: 要爬取的url
    :return: url的所有html字符串
    """
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    output = os.popen("node spider.js %s" % url).read()
    jsonString = json.loads(output)
    hlog.info("爬取完成，返回状态%s" % jsonString["code"])

    html = ""
    if "success" == jsonString["code"]:
        html = jsonString["data"]
    else:
        hlog.debug("爬虫爬取有误")

    hlog.exit_func(func_name)
    return html

def get_start_url():
    """
    根据配置文件设置，获取起始网址
    :return: url获取的网址，num需要爬取的数量
    """
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    headers = {
        "content-type": "application/json"
    }

    url = "http://%s:%s%s"%(
        api_config.source_host,
        api_config.source_port,
        api_config.source_uri
    )
    hlog.var("url", url)
    response = requests.get(url=url, headers= headers)
    if 200 == response.status_code:
        response_string = response.text
        response_json = json.loads(response_string)
        if "SUCCESS" == response_json["code"]:
            hlog.info("获取起始url成功")
            hlog.exit_func(func_name)
            return response_json["result"]["url"], response_json["result"]["num"]

    hlog.debug("获取起始url失败，请检查网络")
    hlog.exit_func(func_name)
    return "", 0

def get_platfrom(url):
    domain = url.split("/")[2]
    platfrom = domain.split(".")[1]
    return platfrom