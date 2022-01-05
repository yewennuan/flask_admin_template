#! /usr/bin/env python
# -*- coding: utf-8 -*-

APP_NAME = 'admin'
ENV = 'testing'
SWAGGER_ENABLE = '/spec'
SIGN_ON = False
SIGN_KEY = '72679f7118537bf2f69ec5466f4bcb69'
IS_SHOW_DEMO = False
HEADER_VERIFY = True
HEADER_PREFIX = 'Admin-'

HEADER_TOKEN = HEADER_PREFIX + 'Token'
HEADER_UID = HEADER_PREFIX + 'Uid'

OPERATION_LOG_PATH = 'logs/operation.log'
CHANNEL_REQUEST_LOG_PATH = 'logs/channel_request.log'
BUSINESS_LOG_INFO_PATH = 'logs/business_info.log'
BUSINESS_LOG_ERROR_PATH = 'logs/business_error.log'
STATISTIC_LOG_PATH = 'logs/statistic.log'
