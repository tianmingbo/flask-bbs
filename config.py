__author__ = '田明博'
__date__ = '2019/9/18 17:54'
import os

# SECRET_KEY = os.urandom(24)  # post提交需要设置SECRET_KEY
SECRET_KEY = 'ccjaskgvksjvk'  # post提交需要设置SECRET_KEY

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
FRONT_USER_ID = 'gdgfsdgsdfg'

# 邮箱配置
# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = "1414518976@qq.com"
MAIL_PASSWORD = "gqtjsezolmmzhced"  # 生成授权码
MAIL_DEFAULT_SENDER = "1414518976@qq.com"

# 发送短信验证码配置
KEY = "LTAI0MNcf8X6BuhW"
SECRET = "qFI9SDlGBfMKlYEIfJSMubJVx2KkDG"

# ueditor使用七牛存储
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "VspB8nq2G1hscVwHWSUp8Jkwx9FBgZ-KkYbdwHce"
UEDITOR_QINIU_SECRET_KEY = "bJlAhvT6dJF-lvolwDK84b5q3q3wLbaSO-IRGTYI"
UEDITOR_QINIU_BUCKET_NAME = "flasksbbs"  # 项目名
UEDITOR_QINIU_DOMAIN = "http://pyfmq94x8.bkt.clouddn.com/"

# 分页设置
PER_PAGE = 10

#celery相关配置
# celery相关的配置
CELERY_RESULT_BACKEND = "redis://:123456@127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://:123456@127.0.0.1:6379/0"