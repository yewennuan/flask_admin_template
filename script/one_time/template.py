#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2021/5/31 14:55

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from admin import create_app

_app = create_app()


def main():
    pass


if __name__ == '__main__':
    main()
