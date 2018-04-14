# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/14 10:03'

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM



def gengerate_random_str(randomlength=8):
    str = ''
    chars = 'QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq0987654321'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str

def send_register_email(email,send_type='register'):
    email_recode = EmailVerifyRecord()
    code = gengerate_random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type =send_type
    email_recode.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '慕雪在线网注册激活'
        email_body = '请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type=='forget':
        email_title = '慕雪在线网密码重置链接'
        email_body = '请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
