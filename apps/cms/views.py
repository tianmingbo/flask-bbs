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

)
import config
from .models import CMSUser
from .forms import LoginForm
from .dectrators import login_requires

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')  # 路由在第一位，不然找不到
@login_requires
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_requires
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_requires
def profile():
    return render_template('cms/cms_profile.html')


class CmsLoginView(views.MethodView):

    def get(self, message=None):
        return render_template('cms/login.html', message=message)

    def post(self):
        form = LoginForm(request.form)  # 使用wtforms
        if form.validate():  # 校验信息
            email = form.email.data  # 拿到信息
            password = form.password.data
            remember = form.remember.data
            user_obj = CMSUser.query.filter_by(email=email).first()
            if user_obj and user_obj.check_password(password):
                # 通过校验,设置session
                session[config.CMS_USER_ID] = user_obj.id  # 设置session
                if remember:  # 是否记住密码
                    session.permanent = True  # session持久化
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或密码错误')
        else:
            message = form.errors.popitem()[1][0]
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=CmsLoginView.as_view('login'))
