#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午1:53
# @Author  : yinxin
# @File    : spider
# @Software: PyCharm

from abc import ABC,abstractmethod


class Spider(ABC):
    start_url = ""
    max_page = 1

    @abstractmethod
    def handle(self):
        pass