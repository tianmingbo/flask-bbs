__author__ = '田明博'
__date__ = '2019/9/18 18:22'
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from exts import db
from apps.cms import models as cms_models
from bbs import create_app

app = create_app()
CMSUser = cms_models.CMSUser

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


if __name__ == '__main__':
    manager.run()
