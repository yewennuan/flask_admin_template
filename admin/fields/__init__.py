#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 16:52
import time

from flask_restx import fields

from admin.rest import card_api


class Timestamp(fields.DateTime):
    __schema_format__ = 'timestamp'
    __schema_type__ = 'integer'

    def __init__(self, dt_format='timestamp', **kwargs):
        super(Timestamp, self).__init__(**kwargs)
        self.dt_format = dt_format

    def format(self, value):
        if isinstance(value, int):
            return value
        if self.dt_format == 'timestamp':
            return int(time.mktime(value.timetuple()))
        return super().format(value)
