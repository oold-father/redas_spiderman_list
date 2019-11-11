#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午1:50
# @Author  : yinxin
# @File    : application
# @Software: PyCharm

from utils import get_start_url,get_platfrom
from common import PLATFORM_SPIDER_MAP

def main():
    url, num = get_start_url()
    # 初始化爬虫
    my_spider = PLATFORM_SPIDER_MAP[get_platfrom(url)](url, num)
    my_spider.handle()

if __name__ == '__main__':
    while True:
        main()

