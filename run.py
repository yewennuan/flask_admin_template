#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from admin import create_app, register_blueprint
from admin.middlewares import record_operation_log, verify_sign_middleware

app = create_app()
register_blueprint(app)


@app.before_request
def verify_sign():
    return verify_sign_middleware()


@app.after_request
def record_rest_log(response):
    # 记录操作日志
    return record_operation_log(response)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) >= 2 else 7070
    app.run(host='0.0.0.0', debug=False, use_reloader=True, port=port)
