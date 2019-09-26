__author__ = '田明博'
__date__ = '2019/9/18 17:57'
from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
import shortuuid
import enum
from datetime import datetime


class GenderEnum(enum.Enum):
    MALE = 1
    FAMALE = 2
    SECRET = 3
    UNKNOW = 4


class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    telephone = db.Column(db.String(11), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True)
    realname = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    gender = db.Column(db.Enum(GenderEnum), default=GenderEnum.UNKNOW)
    join_time = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, *args, **kwargs):
        if 'passwprd' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')
        super(FrontUser, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)  # 对密码加密

    def check_password(self, raw_password):  # 检查密码
        return check_password_hash(self.password, raw_password)
