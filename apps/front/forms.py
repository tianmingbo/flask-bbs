__author__ = '田明博'
__date__ = '2019/9/18 17:58'

from wtforms import Form


class BaseForm(Form):
    '''
    返回一个随机的错误，不返回全部
    '''

    def get_error(self):
        message = self.errors.popitem()[1][0]  # 获取字典中任意一项的value
        return message
