#! /usr/bin/env python
# -*- coding: utf-8 -*-
from admin.util.response import ResponseCode, ResponseCodeExplain


class BaseInternalException(Exception):
    message = ""
    code = ResponseCode.FAIL

    def __init__(self, code=None, message=""):
        if message:
            self.message = message
        if code:
            self.code = code

        if not message and code:
            self.message = ResponseCodeExplain.get(code, '')
