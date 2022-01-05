#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 16:58
from flask_login import current_user, login_required
from flask_restx import Namespace

from admin.fields import input, output
from admin.handler.user import UserHandler
from admin.rest import admin_parser, MyResource
from admin.util.response import response

api = Namespace('/users', description='用户模块')


@api.route("")
@api.expect(admin_parser)
class UsersResource(MyResource):

    @login_required
    @api.marshal_with(output.user_fields)
    def get(self):
        """获取用户信息"""
        result = UserHandler.get_user_info(current_user.get_id())
        return response(data=result)


@api.route("/login")
class UserLoginResource(MyResource):

    @api.expect(input.login_field)
    @api.marshal_with(output.login_fields)
    def post(self):
        """登陆或者注册或者忘记密码"""
        payload = self.payload
        result = UserHandler.login(**payload)
        return response(data=result)


