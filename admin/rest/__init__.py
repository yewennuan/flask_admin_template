#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 14:45

from bson import ObjectId
from flask import g, request
from flask_restx import Api, Resource
from flask_restx.reqparse import RequestParser

from admin.util.exceptions import BaseInternalException
from admin.util.response import response
from admin.util.sign import CardSign
from settings import SWAGGER_ENABLE, HEADER_UID, HEADER_TOKEN, HEADER_VERIFY, SIGN_KEY


class MyResource(Resource):

    def _init_g(self):
        g.token = request.headers.get(HEADER_TOKEN)
        g.uid = request.headers.get(HEADER_UID)

    def dispatch_request(self, *args, **kwargs):
        self._init_g()
        resp = super().dispatch_request(*args, **kwargs)
        if isinstance(resp, dict):
            base_str = CardSign.gen_base_str(resp=resp)
            sign = CardSign.sign(base_str, SIGN_KEY)
            resp['sign'] = sign
        return resp

    @property
    def payload(self):
        kwargs = request.get_json().copy()
        kwargs.pop('sign', '')
        kwargs.pop('timestamp', -1)
        return kwargs

# def permission_required(func):
#     """被该装饰器装饰的接口需要会员才能访问"""
#
#     @wraps(func)
#     def decorated_view(*args, **kwargs):
#
#         if current_user.is_authenticated:
#             if current_user.vip_type != VipType.VIP:
#                 return jsonify({'code': ResponseCode.FORBIDDEN, 'msg': 'you must be vip'})
#         return func(*args, **kwargs)
#
#     return decorated_view


def objectId(value):
    """objectId校验"""
    if value and not ObjectId.is_valid(value):
        raise ValueError('This is not valid objectId')
    return value


card_api = Api(
    prefix='/admin/api', doc=SWAGGER_ENABLE, title="card后台",
    description="admin Api接口定义", version='1.0.0',
)


def gen_parser():
    p = card_api.parser()
    p.add_argument(HEADER_UID, location='headers', required=True, type=objectId, help='用户id')
    p.add_argument(HEADER_TOKEN, location='headers', required=True, type=str, help='token')
    return p


admin_parser = gen_parser()


from admin.rest.user import api as ns_user
from admin.rest.unsign import api as ns_unsign

card_api.add_namespace(ns_user, path='/users')
card_api.add_namespace(ns_unsign, path='/unsign')


@card_api.errorhandler(BaseInternalException)
def handle_base_internal_exception(error):
    return response(code=error.code, msg=error.message), 200
