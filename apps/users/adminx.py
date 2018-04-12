# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 16:57'

import xadmin
from .models import EmailVerifyRecord,Banner
from xadmin import views
# 这里要继承object，不能继承models.Model

# 这两个类要在Users应用中加入，设置后台页面，主题和开头和网页尾部信息
class BaseSetting(object):
    """后台管理的基础配置"""
    enable_themes = True    # 主题配置
    use_bootswatch = True    # 使用boot中的主题


class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'
    # 将旁边展开的模型字段收起来
    menu_style = 'accordion'

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
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)