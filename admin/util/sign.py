#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020-01-15 17:23
import base64
import hashlib
import hmac
import operator
import re

from settings import SIGN_ON, SWAGGER_ENABLE


class CardSign:
    SKIP_SIGN_URL_RE = [
        '.*?/spec',
        '.*?/swagger.json',
        '.*?/swaggerui/.*',
        '.*?/unsign/.*',
    ]

    @classmethod
    def is_skip_sign(cls, request_url=None):
        if not SIGN_ON:
            return True

        if request_url and SWAGGER_ENABLE:
            for url_re in cls.SKIP_SIGN_URL_RE:
                if re.match(url_re, request_url):
                    return True

    @classmethod
    def gen_sorted_str(cls, value):
        if value is None:
            return ''
        elif isinstance(value, list):
            return ','.join([cls.gen_sorted_str(item) for item in value])
        elif isinstance(value, dict):
            sorted_param_list = ['%s=%s' % (k, cls.gen_sorted_str(v)) for k, v in
                                 sorted(value.items(), key=operator.itemgetter(0))]
            str_to_sign = '&'.join(sorted_param_list)
            return str_to_sign
        else:
            return str(value)

    @classmethod
    def gen_base_str(cls, headers=None, params=None, bodies=None, resp=None):
        return cls.gen_sorted_str(headers) + cls.gen_sorted_str(params) + cls.gen_sorted_str(
            bodies) + cls.gen_sorted_str(resp)

    @classmethod
    def sign(cls, base_str, key):
        return base64.standard_b64encode(
            hmac.new(
                key.encode('utf-8'),
                base_str.encode('utf-8'),
                hashlib.sha1).digest()
        ).decode('utf-8')
