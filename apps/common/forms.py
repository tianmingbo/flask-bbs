__author__ = '田明博'
__date__ = '2019/9/24 21:45'

from wtforms import form, StringField
from wtforms.validators import Regexp, InputRequired
from ..forms import BaseForm
import hashlib


class SmsForm(BaseForm):
    salt = 'tianmingboisagoodman'
    telephone = StringField(validators=[Regexp(r'1[3456789]\d{9}')])
    timestamp = StringField(validators=[Regexp(r'\d{13}')])  # 时间戳总共有13位
    sign = StringField(validators=[InputRequired()])  # 签名

    def validate(self):
        result = super(SmsForm, self).validate()
        if not result:
            # 执行父类中的方法，即先验证上述规则有没有通过
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data
        # md5(timestamp+telphone+salt)
        # md5函数必须要传一个bytes类型的字符串进去
        sign2 = hashlib.md5((timestamp + telephone + self.salt).encode('utf-8')).hexdigest()
        if sign == sign2:
            return True
        else:
            return False
