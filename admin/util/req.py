#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020-02-04 11:21
import logging

import requests

from admin.util.exceptions import BaseInternalException
from admin.util.response import ResponseCode

logger = logging.getLogger('channel_request_log')


def get(url, params=None, **kwargs):
    if kwargs.pop('no_encoding', None):
        params = "&".join("{}={}".format(k, v) for k, v in params.items())
    try:
        resp = requests.get(url, params=params, verify=False, **kwargs)
    except requests.exceptions.ConnectionError as e:
        logger.error(e, exc_info=True)
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL, message='connection refused')
    except requests.exceptions.ReadTimeout as e:
        logger.error(e, exc_info=True)
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL, message='connection timeout')
    log = {
        "status": resp.status_code,
        "url": url,
        "method": 'GET',
        "content": resp.text
    }
    if params:
        log['params'] = params
    if kwargs:
        log['kwargs'] = kwargs
    logger.info(json.dumps(log, ensure_ascii=False))
    if resp.status_code != requests.codes.ok:
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL)
    return resp


def post(url, data=None, jsn=None, **kwargs):
    try:
        resp = requests.post(url, data=data, json=jsn, verify=False, **kwargs)
    except requests.exceptions.ConnectionError as e:
        logger.error(e, exc_info=True)
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL, message='connection refused')
    except requests.exceptions.ReadTimeout as e:
        logger.error(e, exc_info=True)
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL, message='connection timeout')
    status = resp.status_code
    log = {
        "status": status,
        "url": url,
        "method": 'POST',
        "content": resp.text
    }
    if data:
        log['data'] = data
    if jsn:
        log['json'] = jsn
    if kwargs:
        log['kwargs'] = kwargs

    logger.info(json.dumps(log, ensure_ascii=False))
    if status != requests.codes.ok:
        raise BaseInternalException(code=ResponseCode.HTTP_RESPONSE_FAIL)
    return resp


if __name__ == '__main__':
    u = 'https://iopen.game.oppomobile.com/sdkopen/user/fileIdInfo'
    p = {
        'fileId': '537762805',
        'token': 'TICKET_0c4GQtEKvjJah49jZl%2F%2B4OBgvyeqSjCwPDWKS30r9nJmUnUxmdYxsMJac9psGMTF',
    }
    p = "&".join("%s=%s" % (k, v) for k, v in p.items())
    headers = {
        'param': 'oauthConsumerKey=d5cf1e30bcc14701b9db27a8454bcb6f&oauthToken=TICKET_0c4GQtEKvjJah49jZl%2F'
                 '%2B4OBgvyeqSjCwPDWKS30r9nJmUnUxmdYxsMJac9psGMTF&oauthSignatureMethod=HMAC-SHA1&oauthTimestamp'
                 '=1581665997&oauthNonce=62639203&oauthVersion=1.0&',
        'oauthSignature': 'cH2vOE1ulq%2Bsye8PCjCrl1Z3vd8%3D'
    }
    r = requests.get(u, params=p, headers=headers)
    print(r.text)
