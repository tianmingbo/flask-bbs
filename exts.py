__author__ = '田明博'
__date__ = '2019/9/18 17:54'
'''
扩展文件，防止循环引用
'''
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()  ## 通过db操作数据库。初始化
mail = Mail()
