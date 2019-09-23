__author__ = '田明博'
__date__ = '2019/9/20 18:05'
from flask import session, g
import config
from .views import bp
from .models import CMSUser


@bp.before_request
def before_request():  # 钩子函数，通过全局变量g，可以向前端传递用户信息
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)  # 获取用户id
        user = CMSUser.query.get(user_id)
        if user:
            g.cms_user = user
