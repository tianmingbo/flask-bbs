__author__ = '田明博'
__date__ = '2019/9/24 20:14'
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import config


def send_sms(telephone, captcha):
    client = AcsClient(config.KEY, config.SECRET, 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    # request.add_query_param('PhoneNumbers', telephone)
    request.add_query_param('SignName', "flask论坛")
    request.add_query_param('TemplateCode', "SMS_174806057")
    code = {}
    code['code'] = captcha
    request.add_query_param('TemplateParam', code)

    response = client.do_action(request)
    # python2:  print(response)
    return str(response, encoding='utf-8')

