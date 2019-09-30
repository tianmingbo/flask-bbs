__author__ = '田明博'
__date__ = '2019/9/25 20:43'

from exts import db
from datetime import datetime


class BannerModel(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now)


class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))  # 帖子属于哪个板块
    author_id = db.Column(db.String(100), db.ForeignKey('front_user.id'), nullable=False)  # 属于哪个作者

    board = db.relationship("BoardModel", backref='posts')  # 反向查询使用
    author = db.relationship('FrontUser', backref='posts')


class HighLightPostModel(db.Model):
    __tablename__ = 'highlight_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    post = db.relationship('PostModel', backref='highlight')  # 帖子加精


class CommentModel(db.Model):
    __tablename__ = 'artile_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))  # 帖子id
    author_id = db.Column(db.String(100), db.ForeignKey('front_user.id'), nullable=False)  # 作者id

    post = db.relationship('PostModel', backref='comments')
    author = db.relationship('FrontUser', backref='comments')
