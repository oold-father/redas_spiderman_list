#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午12:35
# @Author  : yinxin
# @File    : common
# @Software: PyCharm

from pathlib import PurePath
from happy_python import HappyConfigParser
from happy_python import HappyLog
from config import ApiConfig


# 配置文件位置
CONFIG_DIR = PurePath(__file__).parent / 'configs'
CONFIG_FILENAME = str(CONFIG_DIR / 'common.ini')
LOG_CONFIG_FILENAME = str(CONFIG_DIR / 'log.ini')

# 加载api配置
api_config = ApiConfig()
HappyConfigParser.load(CONFIG_FILENAME, api_config)

# 加载log配置
hlog = HappyLog.get_instance(LOG_CONFIG_FILENAME)

