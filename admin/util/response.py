#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: yewennuan
# @Mail: ywnjohu@gmail.com
# @date: 2020/7/24 15:13


class ResponseCode(object):
    # 特殊状态码  0-99
    # 请求成功
    SUCCESS = 0
    # 请求失败
    FAIL = 1
    # 未知错误
    UNKNOWN_ERROR = 4
    # 服务器内部错误
    INTERNAL_ERROR = 5
    # 数据库错误
    DATABASE_ERROR = 6

    # 通用状态码 1000 —— 1999
    # 未认证 请登录
    UNAUTHORIZED = 1001
    # 参数错误
    INVALID_PARAMS = 1002
    # 没有权限
    FORBIDDEN = 1003
    # 版本太低
    APP_VERSION_TOO_LOW = 1004
    # 方法不支持
    METHOD_NOT_ALLOWED = 1005
    # 接口不可用
    API_CLOSED = 1006
    # 数据不存在
    DATA_NOT_EXIST = 1007
    # 签名错误
    SIGN_ERROR = 1008
    # 时间戳超时
    TIME_OUT = 1009
    # 设备被踢出
    DEVICE_KICKED = 1010
    # 数据已存在
    DATA_EXIST = 1011

    # 用户业务相关状态码  2000 —— 2999
    VERIFY_CODE_ERROR = 2000
    USER_EXISTS_ERROR = 2001
    USER_NOT_FOUND_ERROR = 2002
    USER_UPDATED_ERROR = 2003
    USER_DELETED_FAILURE_ERROR = 2004
    REQUIRE_MOBILE = 2005
    GET_WECHAT_INFO_ERROR = 2006
    MOBILE_VERIFY_ERROR = 2007
    INVALID_MOBILE = 2008
    USER_FORBIDDEN = 2009
    USER_NICKNAME_INVALID = 2010  # 用户昵称违规非法
    USER_PASSWORD_ERROR = 2011  # 用户密码错误

    # 付费业务相关错误  3000 —— 3999
    ACCESS_APP_FORBIDDEN = 3000
    MATRIX_INTERNAL_ERROR = 3001
    MATRIX_ORDER_NOT_EXISTS = 3003
    QUOTA_USED_UP = 3004
    DEVICE_USED_UP = 3005
    LIMITED_DAY_USED_UP = 3006
    VIP_TYPE_NOT_ALLOWED = 3007
    TRAIL_EXCHANGED = 3008
    PRODUCT_NOT_READY = 3012
    UNSUBSCRIBE_IOS_PAY_FAIL = 3015
    UNSUBSCRIBE_IOS_SUBSCRIBE_FAIL = 3016

    # 4000 - 4999 for third party marketinterface
    HUAWEI_IAD_INTERNAL_ERROR = 4000

    HTTP_RESPONSE_FAIL = 5000

    WX_BUSINESS_ERROR = 6000


ResponseCodeExplain = {
    ResponseCode.SUCCESS: u'请求成功',
    ResponseCode.UNAUTHORIZED: u'请先登录',
    ResponseCode.INVALID_PARAMS: u'参数不合法',
    ResponseCode.APP_VERSION_TOO_LOW: u'APP版本过低，请更新版本',
    ResponseCode.METHOD_NOT_ALLOWED: u'请求方法不支持',
    ResponseCode.FAIL: u'请求失败',
    ResponseCode.INTERNAL_ERROR: u'服务器内部错误',
    ResponseCode.FORBIDDEN: u'没有权限',
    ResponseCode.API_CLOSED: u'接口不可用',
    ResponseCode.DATA_NOT_EXIST: u'数据不存在',
    ResponseCode.DATA_EXIST: u'数据已存在',
    ResponseCode.SIGN_ERROR: u'签名错误',
    ResponseCode.TIME_OUT: u'时间戳超时',
    ResponseCode.DEVICE_KICKED: u'设备被踢出， 请重新登录',
    ResponseCode.UNKNOWN_ERROR: u'未知错误',
    ResponseCode.VERIFY_CODE_ERROR: u'验证码错误',
    ResponseCode.USER_EXISTS_ERROR: u'用户已经存在',
    ResponseCode.USER_NOT_FOUND_ERROR: u'用户不存在',
    ResponseCode.USER_UPDATED_ERROR: u'更新用户信息失败',
    ResponseCode.USER_DELETED_FAILURE_ERROR: u'删除用户失败',
    ResponseCode.REQUIRE_MOBILE: u'需要绑定手机号',
    ResponseCode.GET_WECHAT_INFO_ERROR: u'获取微信信息失败',
    ResponseCode.MOBILE_VERIFY_ERROR: u'手机号校验失败',
    ResponseCode.DATABASE_ERROR: u'数据库错误',
    ResponseCode.INVALID_MOBILE: u'手机号不合法',
    ResponseCode.USER_FORBIDDEN: u'用户被禁用',
    ResponseCode.USER_NICKNAME_INVALID: u'您的昵称包含违规内容，可能引起儿童不适，请修改！',
    ResponseCode.ACCESS_APP_FORBIDDEN: u'访问应用受限',
    ResponseCode.MATRIX_INTERNAL_ERROR: u'计费内部错误',
    ResponseCode.MATRIX_ORDER_NOT_EXISTS: u'支付订单不存在',
    ResponseCode.PRODUCT_NOT_READY: u'商品缺少必要信息， 不能上架',
    ResponseCode.UNSUBSCRIBE_IOS_PAY_FAIL: u'ios暂不支持退款操作',
    ResponseCode.UNSUBSCRIBE_IOS_SUBSCRIBE_FAIL: u'ios取消订阅请前往itunes操作',
    ResponseCode.HUAWEI_IAD_INTERNAL_ERROR: u'华为服务异常，请稍后再试',
    ResponseCode.HTTP_RESPONSE_FAIL: u'http response error',
    ResponseCode.WX_BUSINESS_ERROR: u'微信业务错误',
}


def response(code=ResponseCode.SUCCESS, msg=None, data=None, meta=None):
    result = {
        'code': code,
        'msg': msg or ResponseCodeExplain.get(code, '')
    }

    if code == ResponseCode.SUCCESS:
        if data is not None:
            result.update(dict(data=data))
        if meta is not None:
            result.update(dict(meta=meta))

    return result
