#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020-01-20 17:20
import logging
import os

from admin.common.define import EnvType
from settings import OPERATION_LOG_PATH, BUSINESS_LOG_INFO_PATH, BUSINESS_LOG_ERROR_PATH, ENV
from admin.util.log import InfoFilter

if not os.path.exists(os.path.dirname(OPERATION_LOG_PATH)):
    os.makedirs(os.path.dirname(OPERATION_LOG_PATH))

if not os.path.exists(os.path.dirname(BUSINESS_LOG_INFO_PATH)):
    os.makedirs(os.path.dirname(BUSINESS_LOG_INFO_PATH))

if not os.path.exists(os.path.dirname(BUSINESS_LOG_ERROR_PATH)):
    os.makedirs(os.path.dirname(BUSINESS_LOG_ERROR_PATH))

if ENV == EnvType.PROD:
    console_log_level = logging.INFO
else:
    console_log_level = logging.DEBUG
logging_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'info_filter': {
            '()': InfoFilter,
        },

    },
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(name)s %(process)d %(message)s',
        },
        'operation': {
            'format': '%(asctime)s %(message)s',
        },
    },
    'root': {
        'handlers': ['console', 'business_info', 'business_error'],
        'level': console_log_level,
    },
    'loggers': {
        'admin': {
            'handlers': ['console', 'business_info', 'business_error'],
            'propagate': False,
            'level': console_log_level,
        },
        'operation_log': {
            'handlers': ['operation'],
            'propagate': False,
            'level': logging.INFO,
        },
    },
    'handlers': {
        'console': {
            'level': console_log_level,
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'stream': 'ext://sys.stdout',
        },
        'operation': {
            'level': console_log_level,
            'class': 'logging.handlers.SafeTimedRotatingFileHandler',
            'encoding': 'utf-8',
            'formatter': 'operation',
            'filename': OPERATION_LOG_PATH,
            'backupCount': 120,
            'when': 'MIDNIGHT',
        },
        'business_info': {
            'level': console_log_level,
            'class': 'logging.handlers.SafeTimedRotatingFileHandler',
            'encoding': 'utf-8',
            'formatter': 'console',
            'filename': BUSINESS_LOG_INFO_PATH,
            'filters': ['info_filter'],
            'backupCount': 30,
            'when': 'MIDNIGHT',
        },
        'business_error': {
            'level': logging.ERROR,
            'class': 'logging.handlers.SafeTimedRotatingFileHandler',
            'encoding': 'utf-8',
            'formatter': 'console',
            'filename': BUSINESS_LOG_ERROR_PATH,
            'backupCount': 30,
            'when': 'MIDNIGHT',
        },
    },
}
