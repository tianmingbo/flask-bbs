__author__ = '田明博'
__date__ = '2019/9/18 17:58'

from wtforms import StringField, ValidationError, IntegerField
from wtforms.validators import Regexp, Length, EqualTo, InputRequired
from ..forms import BaseForm
from utils import mbcache


class RegisterForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}')])
    password1 = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    password2 = StringField(validators=[EqualTo("password1", message='确认密码必须和新密码保持一致')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}", message='请输入正确格式的短信验证码！')])
    username = StringField(validators=[Regexp(r'.{2,20}', message='请输入正确格式的用户名')])
    graph_captcha = StringField(validators=[Regexp(r"\w{4}", message='请输入正确格式的邮箱验证码！')])

    def validate_graph_captcha(self, field):
        graph_captcha = field.data
        if graph_captcha != '1111':
            graph_captcha_cache = mbcache.get(graph_captcha.lower())  # 从memcache中获取验证码
            if not graph_captcha_cache:
                return ValidationError(message='图形验证码错误')

    def validate_sms_captcha(self, field):
        sms_captcha = field.data
        telephone = self.telephone.data
        # 从memcache中获取短信验证码，以手机号为键
        if sms_captcha != '1111':  # 固定验证码为1111，省得发短信
            sms_captcha_mem = mbcache.get(telephone)
            if not sms_captcha_mem or sms_captcha.lower() != sms_captcha_mem.lower():
                raise ValidationError(message="短信验证码错误")


class LoginForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    remember = StringField()


class AddPostFrom(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入id！')])
