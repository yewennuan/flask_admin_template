#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 16:53
from flask_restx import fields

from admin.fields import Timestamp
from admin.rest import card_api

next_obj = card_api.model('NextObj', {
    "offset": fields.Integer(required=True),
    "limit": fields.Integer(required=True)
})

meta = card_api.model('Meta', {
    "total": fields.Integer(required=True),
    "next": fields.Nested(next_obj)
})

base = card_api.model('Base', {
    'code': fields.Integer(required=True),
    'msg': fields.String(required=True),
    'sign': fields.String(required=True),
})

base_page = card_api.inherit('BaseList', base, {
    'meta': fields.Nested(meta, skip_none=True)
})

user = card_api.model('User', {
    'id': fields.String(required=True),
    'email': fields.String(required=True),
    'username': fields.String(required=True),
    'avatar': fields.String(required=False),
    'created_at': Timestamp(required=True),
})

login = card_api.model('LoginResp', {
    'token': fields.String(required=True),
    'user': fields.Nested(user, skip_none=True)
})

login_fields = card_api.inherit('LoginRespField', base, {
    'data': fields.Nested(login, skip_none=True)
})

user_fields = card_api.inherit('UserRespField', base, {
    'data': fields.Nested(user, skip_none=True)
})