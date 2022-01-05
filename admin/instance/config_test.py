#! /usr/bin/env python
# -*- coding: utf-8 -*-

# flask
SECRET_KEY = 'THIS IS NEED TO BE SECRET'
DEBUG = True


# flask login
LOGIN_DISABLED = False

SWAGGER_UI_DOC_EXPANSION = 'list'
# SWAGGER_UI_DOC_EXPANSION = 'none'
RESTX_VALIDATE = True
RESTX_MASK_SWAGGER = False
RESTX_ERROR_404_HELP = False
ERROR_INCLUDE_MESSAGE = False

# flask mongoengine
MONGODB_SETTINGS = {
    'db': 'admin',
    'host': 'mongodb://127.0.0.1:27017/admin',
}

# flask cache
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = 'localhost'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = 1

MY_REDIS_DB = 0
