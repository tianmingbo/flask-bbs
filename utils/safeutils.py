__author__ = '田明博'
__date__ = '2019/9/25 17:26'
from urllib.parse import urlparse, urljoin
from flask import request


def is_safe_url(target):
    ref_url = urlparse(request.host_url)  # 对域名进行解析
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
