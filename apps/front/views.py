__author__ = '田明博'
__date__ = '2019/9/18 17:57'
from flask import (Blueprint,
                   views,
                   g,
                   session,
                   render_template,
                   redirect,
                   make_response,
                   request,
                   url_for,
                   abort,

                   )
import config
from exts import db
from sqlalchemy.sql import func
from flask_paginate import Pagination, get_page_parameter
from .forms import RegisterForm, LoginForm, AddPostFrom
from .models import FrontUser
from utils import restful, safeutils
from apps.models import BannerModel, PostModel, BoardModel, CommentModel
from .dectrators import login_requires
from apps.models import HighLightPostModel

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    bd = request.args.get('bd', type=int, default=None)  # 获取当前板块
    st = request.args.get('st', type=int, default=1)  # 获取排序规则
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()  # 所有轮播图

    boards = BoardModel.query.all()  # 所有板块
    # 分页设置
    page = request.args.get(get_page_parameter(), type=int, default=1)  # 没有page参数，默认值为1
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE

    item_post = None
    if st == 1:
        item_post = PostModel.query.order_by(PostModel.create_time.desc())  # 降序排序
    elif st == 2:
        item_post = db.session.query(PostModel).outerjoin(HighLightPostModel).order_by(
            HighLightPostModel.create_time.desc(), PostModel.create_time.desc())  # 按照加精排序
    elif st == 3:
        item_post = PostModel.query.order_by(PostModel.create_time.desc())
    elif st == 4:
        item_post = db.session.query(PostModel).outerjoin(CommentModel).group_by(PostModel.id).order_by(
            func.count(CommentModel.id).desc(), PostModel.create_time.desc())
    if bd:
        item_post = item_post.filter(PostModel.board_id == bd)
        posts = item_post.slice(start, end)
        total = item_post.count()
    else:
        posts = item_post.slice(start, end)
        total = item_post.count()

    # bs_version：bootstramp版本，，，outer_window：省略号前和后有几个选项
    pagination = Pagination(bs_version=3, page=page, total=total,
                            outer_window=0, inner_window=2)

    context = {
        'banners': banners,
        'boards': boards,
        'posts': posts,
        'pagination': pagination,
        'current_board': bd,
        'current_sort': st
    }
    return render_template('front/index.html', **context)


@bp.route('/logout/')
@login_requires
def logout():
    del session[config.FRONT_USER_ID]  # 删除session中存储的信息，没有则不保持登录状态
    return redirect('/login/')  # 重定向到登录页面


@bp.route('/apost/', methods=['GET', 'POST'])
@login_requires
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()

        return render_template('front/write.html', boards=boards)
    else:
        form = AddPostFrom(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.params_error(message='没有这个板块！')
            post = PostModel(title=title, content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


@bp.route('/p/<post_id>')
def post_detail(post_id):
    post_obj = PostModel.query.get(post_id)
    if not post_obj:
        abort(404)
    return render_template('front/p_detail.html', post=post_obj)


@bp.route('/add_comment/', methods=['POST'])
@login_requires
def add_comment():
    content = request.form.get('content')
    post_id = request.form.get('post_id')
    print(content, post_id)
    post_obj = PostModel.query.get(post_id)
    if not post_obj:
        return restful.params_error(message='没有这个帖子！')
    # 添加评论数据
    comment_obj = CommentModel(content=content)
    comment_obj.post = post_obj
    comment_obj.author = g.front_user
    db.session.add(comment_obj)
    db.session.commit()
    return restful.success()


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        else:
            return render_template('front/front_signup.html')

    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = FrontUser(password=password, username=username, telephone=telephone)
            db.session.add(user)
            db.session.commit()  # 提交
            return restful.success()  # 返回提示信息
        else:
            return restful.params_error(message=form.get_error())


class LoginView(views.MethodView):

    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id

                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='手机号或密码错误！')
        else:
            return restful.params_error(message=form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
