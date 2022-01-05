#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2021/1/13 下午9:08
from admin import User
from admin.util.exceptions import BaseInternalException
from admin.util.response import ResponseCode


class UserHandler:

    @classmethod
    def get_user_info(cls, uid):
        return User.get_by_id(uid)

    @classmethod
    def login(cls, email, password_md5):
        user = User.get_by_email(email)
        if not user:
            raise BaseInternalException(code=ResponseCode.UNKNOWN_ERROR, message='账号或者密码错误')
        if not user.verify_password(password_md5):
            raise BaseInternalException(code=ResponseCode.UNKNOWN_ERROR, message='账号或者密码错误')
        return dict(token=user.generate_user_token(), user=user)

