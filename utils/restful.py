__author__ = '田明博'
__date__ = '2019/9/21 20:00'

'''
优化json数据的返回值
'''
from flask import jsonify


class HttpCode(object):
    ok = 200
    unautherror = 401
    paramserror = 400  # 参数错误
    servererror = 500  # 服务器错误


def resuful_result(code, message, data):
    return jsonify({"code": code, "message": message, "data": data or {}})


def success(message="", data=None):
    return resuful_result(code=HttpCode.ok, message=message, data=data)


def unauth_error(message=""):
    return resuful_result(code=HttpCode.unautherror, message=message, data=None)


def params_error(message=""):
    return resuful_result(code=HttpCode.paramserror, message=message, data=None)


def server_error(message=""):
    return resuful_result(code=HttpCode.servererror, message=message, data=None)
