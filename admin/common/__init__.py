#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 14:50


class Enum(object):

    @classmethod
    def choices(cls):
        return [v for k, v in cls.__dict__.items() if k.isupper()]

    @classmethod
    def desc(cls):
        return '; '.join(
            ['{}:{}'.format(v, k) for k, v in cls.__dict__.items()
             if k.isupper()]
        )
