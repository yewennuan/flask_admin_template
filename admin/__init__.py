#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2021/1/7 上午11:20

import logging.config
import os

import redis
from flask import Flask
from flask_caching import Cache
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

from admin.instance.config import MY_REDIS_DB, CACHE_REDIS_PORT, CACHE_REDIS_HOST
from admin.instance.logging_config import logging_dict
from admin.models.user import User
from settings import HEADER_TOKEN
login_manager = LoginManager()
cache = Cache()
redis_client = redis.Redis(host=CACHE_REDIS_HOST, port=CACHE_REDIS_PORT, db=MY_REDIS_DB)


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)


@login_manager.request_loader
def load_user_from_request(request):
    token = request.headers.get(HEADER_TOKEN, '')
    if not token:
        return None
    user = User.verify_auth_token(token)
    return user


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    base_dir = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(base_dir, 'instance', 'config.py')
    app.config.from_pyfile(config_file)
    MongoEngine(app)
    login_manager.init_app(app)
    cache.init_app(app)
    init_log()
    return app


def register_blueprint(app):
    # 将所有命名空间注册
    from admin.rest import card_api
    card_api.init_app(app)
    return app


def init_log():
    logging.config.dictConfig(logging_dict)
