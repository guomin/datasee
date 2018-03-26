#!/usr/bin/env python
# coding=utf-8

# -----------------------------------
# Author: guomin - guomin05@baidu.com
# Created Time : 一  3/26 14:06:31 2018

# File Name: utils/Utils.py
# Description:

# ----------------------------------
import requests
import logging
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

__logger_name__ = "django.%s" % __name__
logger = logging.getLogger(__logger_name__)
