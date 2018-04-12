# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 16:57'

import xadmin
from .models import EmailVerifyRecord,Banner

# 这里要继承object，不能继承models.Model


class EmailVerifyRecordAdmin(object):
    # 显示的字段列
    list_display = ['code','email','send_type','send_time']
    # 搜索
    search_fields = ['code','email','send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)