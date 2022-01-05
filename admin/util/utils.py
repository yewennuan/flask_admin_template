#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 16:17
import base64
import json
import logging
import random

logger = logging.getLogger(__name__)


def decrypt_token(token):
    try:
        args_str = base64.b64decode(token)
    except Exception as e:
        logger.error('token: {} decode出错, error:{}'.format(token, e))
        return {}
    if not args_str:
        return {}
    return json.loads(args_str)


def decrypt_ext(ext):
    if not ext:
        return {}
    try:
        args_str = base64.b64decode(ext)
        return json.loads(args_str)
    except Exception:
        pass
    return {}


def gen_random_num(length=6):
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    random.shuffle(items)
    return ''.join(items[0:length])


def pagination(total, limit, offset, data=None):
    page_next = total > limit + offset and dict(limit=limit, offset=limit + offset) or None
    meta = dict(next=page_next, total=total)
    if data and isinstance(data, list):
        last_modified = 0
        for item in data:
            last_modified = max(last_modified, item.get('updated_at', 0))
        meta['updated_at'] = last_modified
    return meta

