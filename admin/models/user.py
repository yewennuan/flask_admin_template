#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2021/1/8 下午6:16
import logging
from datetime import datetime

from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
from mongoengine import Document, StringField, DateTimeField, IntField, DictField
from werkzeug.security import generate_password_hash, check_password_hash

from admin.common.define import Constant

logger = logging.getLogger(__name__)


class User(UserMixin, Document):
    """用户"""
    username = StringField(max_length=256, default='')
    email = StringField(required=True)
    password_hash = StringField(default='')
    avatar = StringField(default='')
    last_login_at = DateTimeField(required=True, default=datetime.now)
    created_at = DateTimeField(required=True, default=datetime.now)
    updated_at = DateTimeField(required=True, default=datetime.now)

    meta = {
        "collection": 'users',
        "indexes": [
            {
                "fields": ("username",),
            },
            {
                "fields": ("email",),
                "unique": True,
            },
        ],
        "strict": False
    }

    def update_attr(self, password_md5=None, **kwargs):
        if password_md5:
            password_hash = generate_password_hash(password_md5)
            kwargs['password_hash'] = password_hash
        self.modify(updated_at=datetime.now(), **kwargs)
        return self

    @classmethod
    def create(cls, password_md5=None, **kwargs):
        password_hash = ''
        if password_md5:
            password_hash = generate_password_hash(password_md5)
        return cls(password_hash=password_hash, **kwargs).save()

    def verify_password(self, password_md5):
        return check_password_hash(self.password_hash, password_md5)

    @classmethod
    def get_by_id(cls, uid):
        return cls.objects(id=uid).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.objects(email=email).first()

    def generate_user_token(self, expiration=Constant.ONE_WEEK):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        data = {
            'uid': self.get_id(),
        }
        token = s.dumps(data).decode('ascii')
        return token

    @classmethod
    def verify_auth_token(cls, token):
        secret_key = current_app.config['SECRET_KEY']
        s = TimedJSONWebSignatureSerializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except Exception as e:
            logger.error('解析认证token时异常， token:{}, error:{}'.format(token, e))
            return None
        if data and data.get('uid'):
            user = cls.get_by_id(data.get('uid'))
            return user
        return None
