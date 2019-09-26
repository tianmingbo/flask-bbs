# encoding: utf-8
from flask import g
from wtforms import StringField, IntegerField
from wtforms.validators import Email, InputRequired, Length, EqualTo
from wtforms import ValidationError
from ..forms import BaseForm
from utils import mbcache


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6, 20, message='请输入正确格式的密码')])
    remember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的旧密码')])
    newpwd = StringField(validators=[Length(6, 20, message='请输入正确格式的新密码')])
    newpwd2 = StringField(validators=[EqualTo("newpwd", message='确认密码必须和新密码保持一致')])


class ResetEmailForm(BaseForm):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    captcha = StringField(validators=[Length(6, 6, message='请输入正确的验证码')])

    def validate_email(self, field):
        email = field.data
        user = g.cms_user
        if user.email == email:
            raise ValidationError('不能修改为相同的邮箱')

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_cache = mbcache.get(email)  # 从memcach中获取验证码
        if not captcha_cache or captcha.lower() != captcha_cache.lower():  # 不区分大小写
            return ValidationError('验证码错误')


class AddBannerForm(BaseForm):
    name = StringField(validators=[InputRequired(message='请输入轮播图名称！')])
    image_url = StringField(validators=[InputRequired(message='请输入轮播图图片链接！')])
    link_url = StringField(validators=[InputRequired(message='请输入轮播图跳转链接！')])
    priority = IntegerField(validators=[InputRequired(message='请输入轮播图优先级！')])  # 优先级整型

class UpdateBannerForm(AddBannerForm):
    banner_id=IntegerField(validators=[InputRequired(message='请输入轮播图的id！')])

