# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 18:08'

import xadmin
from .models import CityDict,CourseOrg,Teacher

# 这里要继承object，不能继承models.Model


class CityDictAdmin(object):
    # 显示的字段列
    list_display = ['name','desc','add_time']
    # 搜索
    search_fields = ['name','desc']
    # 过滤器
    list_filter = ['name','desc','add_time']


class CourseOrgAdmin(object):
    list_display = ['name','desc','click_nums','fav_nums','image','address','city','add_time']
    search_fields = ['name','desc','click_nums','fav_nums','image','address','city']
    # 外键如何处理，如果只写course，则不能显示，如果想显示，则需要写成course__name(字段名)
    list_filter = ['name','desc','click_nums','fav_nums','image','address','city','add_time']

class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']
    search_fields = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)