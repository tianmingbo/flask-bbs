__author__ = '田明博'
__date__ = '2019/9/18 17:56'
from flask import (
    Blueprint,
    render_template,
    views,
    request,
    redirect,
    url_for,
    session,
    g,
    jsonify,
)
import uuid
from exts import db, mail
from flask_mail import Message
import config
from .models import CMSUser, CMSPersmission
from .forms import LoginForm, ResetpwdForm, ResetEmailForm, AddBannerForm, UpdateBannerForm
from .dectrators import login_requires, primission_require
from utils import restful
from utils import mbcache
from apps.models import BannerModel

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')  # 路由在第一位，不然找不到
@login_requires
def index():
    return render_template('cms/cms_index.html')


@bp.route('/banners/')
@login_requires
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    return render_template('cms/cms_baners.html', banners=banners)


@bp.route('/add_banners/', methods=['POST'])
@login_requires
def add_banners():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/update_banner/', methods=['POST'])
@login_requires
def update_banner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner_id = form.banner_id.data
        print(banner_id)
        banner = BannerModel.query.filter_by(id=banner_id).first()
        print(banner)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='没有这个轮播图')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/delete_banner/', methods=['POST'])
@login_requires
def delete_banner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.params_error(message='没有轮播图id！')  # 甚是不妥
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error(message='没有这个轮播图！')
    db.session.delete(banner)
    db.session.commit()
    return restful.success()  # 返回成功提示


@bp.route('/logout/')
@login_requires
def logout():
    del session[config.CMS_USER_ID]  # 删除session中存储的信息，没有则不保持登录状态
    return redirect(url_for('cms.login'))  # 重定向到登录页面


@bp.route('/profile/')
@login_requires
def profile():
    return render_template('cms/cms_profile.html')  # 个人信息页面


@bp.route('/posts/')
@login_requires
@primission_require(CMSPersmission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_requires
@primission_require(CMSPersmission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_requires
@primission_require(CMSPersmission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_requires
@primission_require(CMSPersmission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_requires
@primission_require(CMSPersmission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_requires
@primission_require(CMSPersmission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


class CmsLoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/login.html', message=message)

    def post(self):
        form = LoginForm(request.form)  # 使用wtforms
        if form.validate():  # 校验信息
            email = form.email.data  # 拿到提交的信息
            password = form.password.data
            remember = form.remember.data
            user_obj = CMSUser.query.filter_by(email=email).first()
            if user_obj and user_obj.check_password(password):
                # 通过校验,设置session
                session[config.CMS_USER_ID] = user_obj.id  # 设置session
                if remember:  # 是否记住密码
                    session.permanent = True  # session持久化
                return redirect(url_for('cms.index'))  # 重定向到主页
            else:
                return self.get(message='邮箱或密码错误')
        else:
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_requires]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                # 如果旧密码存在
                user.password = newpwd
                db.session.commit()  # 保存到数据库
                return restful.success()
            else:
                return restful.params_error('旧密码错误')
        else:
            message = form.get_error()
            return restful.params_error(message)


class ResetEmailView(views.MethodView):
    '''
    修改邮箱，需要先发送验证码确认，获取验证码，输入验证码后才能修改。
    '''
    decorators = [login_requires]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            user = g.cms_user
            user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


@bp.route('/email_captcha/')
@login_requires
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.params_error('请输入邮箱')
    '''
    生成随机验证码，保存到数据库中，然后发送验证码，与用户提交的验证码对比
    '''
    captcha = str(uuid.uuid1())[:6]  # 随机生成6位验证码
    # user = g.cms_user
    # user.catptcha_code = captcha
    # db.session.commit()  # 把验证码保存到数据库/存放在memcached中
    # 给用户提交的邮箱发送邮件
    message = Message('Python论坛邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)

    try:
        mail.send(message)  # 发送
    except:
        return restful.server_error()
    mbcache.set(email, captcha)
    return restful.success()


bp.add_url_rule('/login/', view_func=CmsLoginView.as_view('login'))  # 加到url
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))  # 加到url
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))  # 加到url
