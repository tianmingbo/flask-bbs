__author__ = '田明博'
__date__ = '2019/9/18 18:22'
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models
from apps.models import BannerModel
from bbs import create_app

app = create_app()
CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPermission = cms_models.CMSPersmission

FrontUser = front_models.FrontUser

manager = Manager(app)
# 用来绑定app和db到flask_migrate
Migrate(app, db)
# 添加Migrate的所有子命令到db下
manager.add_command('db', MigrateCommand)


# 自定义创建命令
@manager.option('-e', '--email', dest='email')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_cms_user(email, username, password):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        print('该邮箱已经存在！')
        return
    else:
        user = CMSUser(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        print('CMS用户添加成功！')


@manager.command
def create_role():  # 添加角色和权限，也可手动添加
    # 1. 访问者（可以修改个人信息）
    visitor = CMSRole(name='访问者', desc='只能访问相关数据，不能修改。')
    visitor.permissions = CMSPermission.VISITOR

    # 2. 运营角色（修改个人个人信息，管理帖子，管理评论，管理前台用户）
    operator = CMSRole(name='运营', desc='管理帖子，管理评论,管理前台用户。')
    operator.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER

    # 3. 管理员（拥有绝大部分权限）
    admin = CMSRole(name='管理员', desc='拥有本系统所有权限。')
    admin.permissions = CMSPermission.VISITOR | CMSPermission.POSTER | CMSPermission.CMSUSER | CMSPermission.COMMENTER | CMSPermission.FRONTUSER | CMSPermission.BOARDER

    # 4. 开发者
    developer = CMSRole(name='开发者', desc='开发人员专用角色。')
    developer.permissions = CMSPermission.ALL_PERMISSION

    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):  # 为用户添加权限
    user = CMSUser.query.filter_by(email=email).first()  # 获取用户
    if user:
        role = CMSRole.query.filter_by(name=name).first()  # 获取角色，判断是否有这个角色
        if role:
            role.users.append(user)
            db.session.commit()
            print('用户添加到角色成功！')
        else:
            print('没有这个角色：%s' % role)
    else:
        print('%s邮箱没有这个用户!' % email)


@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)  # 添加
    db.session.commit()


@manager.command
def test_permission():
    user = CMSUser.query.all()[1]
    if user.is_developer:
        print('这个用户有开发者的权限！')
    else:
        print('这个用户没有开发者权限！')


if __name__ == '__main__':
    manager.run()
