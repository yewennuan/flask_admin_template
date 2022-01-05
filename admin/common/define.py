#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 14:50
from admin.common import Enum


class Constant:
    PRICE_RATE = 100
    ONE_MINUTE = 60
    ONE_HOUR = ONE_MINUTE * 60
    ONE_DAY = 24 * ONE_HOUR
    ONE_WEEK = 7 * ONE_DAY
    ONE_YEAR = 365 * ONE_DAY


class EnvType(Enum):
    DEV = 'dev'
    TEST = 'test'
    PROD = 'prod'


class RedisKey:
    USER_ORDER_SYNC_KEY = 'user_order_sync_key_order_no:{}'

