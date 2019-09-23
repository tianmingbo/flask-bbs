__author__ = '田明博'
__date__ = '2019/9/18 17:56'
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CMSPersmission(object):
    # 255的二进制方式来表示 1111 1111
    ALL_PERMISSION = 0b11111111
    # 1. 访问者权限
    VISITOR = 0b00000001
    # 2. 管理帖子权限
    POSTER = 0b00000010
    # 3. 管理评论的权限
    COMMENTER = 0b00000100
    # 4. 管理板块的权限
    BOARDER = 0b00001000
    # 5. 管理前台用户的权限
    FRONTUSER = 0b00010000
    # 6. 管理后台用户的权限
    CMSUSER = 0b00100000
    # 7. 管理后台管理员的权限
    ADMINER = 0b01000000


# 角色和用户是多对多关系，定义一个第三方表
cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id', db.Integer, db.ForeignKey('cms_role.id'), primary_key=True),
    db.Column('cms_user_id', db.Integer, db.ForeignKey('cms_user.id'), primary_key=True),
)


class CMSRole(db.Model):
    __tablename__ = 'cms_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)  # 角色名
    desc = db.Column(db.String(200), nullable=True)  # 描述信息
    create_time = db.Column(db.DateTime, default=datetime.now)
    permissions = db.Column(db.Integer, default=CMSPersmission.VISITOR)  # 权限

    users = db.relationship('CMSUser', secondary=cms_role_user, backref='roles')
    # secondary中间表，backref 反向引用


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

    # catptcha_code = db.Column(db.String(10), default=0, nullable=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)  # 对密码加密

    def check_password(self, raw_password):  # 检查密码
        return check_password_hash(self.password, raw_password)

    @property
    def permissions(self):
        '''
        获取用户的全部权限
        :return:
        '''
        if not self.roles:
            # 没有角色
            return 0
        all_permissions = 0
        for role in self.roles:  # 遍历用户的每个角色
            permissions = role.permissions
            all_permissions |= permissions  # 所有权限
        return all_permissions

    def has_permission(self, permission):
        # 查看有没有某个权限
        return self.permissions & permission == permission  # 与所有权限与运算，判断有没有这个

    @property
    def is_developer(self):
        # 判断用户是不是开发者。判断这个用户是不是有所有权限，返回True，是。反之
        return self.has_permission(CMSPersmission.ALL_PERMISSION)
