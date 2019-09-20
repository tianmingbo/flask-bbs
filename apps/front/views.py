__author__ = '田明博'
__date__ = '2019/9/18 17:57'
from flask import Blueprint

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'front index'
