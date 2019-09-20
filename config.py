__author__ = '田明博'
__date__ = '2019/9/18 17:54'
import os

SECRET_KEY = os.urandom(24)  # post提交需要设置SECRET_KEY

DEBUG = True

# 配置数据库
DB_USERNAME = 'root'
DB_PASSWORD = 'tian'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'sbbs'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'DEFAULT'
