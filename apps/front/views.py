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
                   )
import config
from exts import db
from .forms import RegisterForm, LoginForm
from .models import FrontUser
from utils import restful, safeutils

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return render_template('front/index.html')


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
            user = FrontUser.query.filter_by(telephone=telephone).first()  # 查询有没有这个用户
            if user and user.check_password(password):  # 验证密码
                session[config.FRONT_USER_ID] = user.id  # 把用户id写入session
                if remember:
                    # 持久化
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='信息填写错误')
        else:
            return restful.params_error(message=form.get_error())


bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
