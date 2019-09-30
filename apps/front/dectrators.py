__author__ = '田明博'
__date__ = '2019/9/20 17:02'


from flask import session, redirect, url_for
import config
from functools import wraps


def login_requires(func):
    @wraps(func)
    # 修复装饰器
    def inner(*args, **kwargs):
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.login'))

    return inner
