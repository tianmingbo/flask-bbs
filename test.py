__author__ = '田明博'
__date__ = '2019/9/21 21:37'
# import uuid
# print(str(uuid.uuid1())[:6])
# import string
# import random
#
# # print(''.join(random.choices(list(string.ascii_letters), k=6)))  # 随机获取6位
# source = list(string.ascii_letters)
# source.extend(map(lambda x:str(x),range(0,10)))
# # print(source)
# captcha = "".join(random.sample(source,6))
# print(captcha)
# import shortuuid
# print(shortuuid.uuid())
import config
from flask import session,g
session[config.FRONT_USER_ID]='dddd'
print(session)