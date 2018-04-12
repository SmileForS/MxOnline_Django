# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 16:57'

import xadmin
from .models import EmailVerifyRecord
# 这里要继承object，不能继承models.Model
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)