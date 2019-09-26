__author__ = '田明博'
__date__ = '2019/9/18 17:56'

from flask import Blueprint, request, make_response
from utils.captcha import Captcha
from utils import mbcache, alidayu
from utils import restful, mbcache
from .forms import SmsForm
from io import BytesIO

bp = Blueprint('common', __name__, url_prefix='/c')


@bp.route('/')
def index():
    return 'common index'


@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    mbcache.set(text.lower(), text.lower())
    out = BytesIO()  # 二进制流对象
    image.save(out, 'png')  # 保存在out中
    out.seek(0)  # 文件流的指针放在0位置
    resp = make_response(out.read())  # 读出来
    resp.content_type = 'image/png'  # 指定数据类型
    return resp


# @bp.route('/sms_captcha/', methods=['POST'])
# def sms_captcha():
#     '''
#     发送验证码，调用alidayu中的send_cms
#     :return:
#     '''
#
#     telephone = request.form.get('telephone')
#     if not telephone:
#         return restful.params_error(message='请传入手机号码！')
#
#     captcha = Captcha.gene_text(number=4)
#     print(telephone, captcha)
#     if alidayu.send_sms(telephone, captcha=captcha):
#         return restful.success()
#
#         # return restful.params_error(message='短信验证码发送失败！')
#     return restful.success()
@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SmsForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)

        if alidayu.send_sms(telephone, captcha=captcha):
            # 把验证码放入memcache，与用户提交的对比
            mbcache.set(telephone, captcha)
            return restful.success()
        else:
            mbcache.set(telephone, captcha)
            return restful.success()
    else:
        return restful.params_error(message='参数错误')
