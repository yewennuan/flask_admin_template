#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

from flask import request, jsonify

from admin.util.response import ResponseCode
from admin.util.sign import CardSign
from settings import SIGN_KEY, HEADER_PREFIX, SIGN_ON

operation_logger = logging.getLogger('operation_log')


def record_operation_log(response):
    # 接口日志
    if request.method in ['POST', 'PATCH', 'PUT', 'DELETE']:
        return record(response)

    return response


def record(response):
    log = {
        "status": response.status,
        "url": request.full_path,
        "method": request.method,
    }

    custom_headers = {k: v for k, v in request.headers.items()}
    form = {k: v if len(v) > 1 else v[0] for k, v in request.form.lists()}
    files = [{k: v.filename} for k, v in request.files.items(multi=True)]
    data = request.get_json(silent=True) if request.is_json else None
    resp = response.get_json() if response.is_json else None
    body = {
        'headers': custom_headers,
        'form': form,
        'files': files,
        'json': data,
        'resp': resp,
    }
    log.update(body)
    operation_logger.info(json.dumps(log, ensure_ascii=False))
    return response


def verify_sign_middleware():
    if not SIGN_ON:
        return

    if CardSign.is_skip_sign(request_url=request.url):
        return

    # 不是这些 http method不验签
    if request.method not in ['POST', 'PUT', 'PATCH', 'DELETE']:
        return

    sign_key = SIGN_KEY

    params = request.args
    bodies = request.get_json() if request.is_json else {}
    input_sign = bodies.pop('sign', '')
    headers = {k: v for k, v in request.headers.items() if k.startswith(HEADER_PREFIX)}
    base_str = CardSign.gen_base_str(headers, params, bodies)

    if not input_sign or input_sign != CardSign.sign(base_str, sign_key):
        return jsonify({'code': ResponseCode.SIGN_ERROR, 'msg': 'sign error'})
