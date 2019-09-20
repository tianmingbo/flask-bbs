__author__ = '田明博'
__date__ = '2019/9/18 17:56'

from flask import Blueprint

bp = Blueprint('common', __name__, url_prefix='/common')


@bp.route('/')
def index():
    return 'common index'
