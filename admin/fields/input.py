#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 16:53
from flask_restx import fields

from admin.rest import card_api

extra_payload = {
    'timestamp': fields.Integer(required=True, description='当前时间戳， 精确到秒'),
    'sign': fields.String(required=True, description='签名')
}

extra_fields = card_api.model('ExtraField', extra_payload)

login_field = card_api.inherit('LoginField', extra_fields, {
    'email': fields.String(required=False, description='手机号码'),
    'password_md5': fields.String(required=False, description='密码md5值'),
})
