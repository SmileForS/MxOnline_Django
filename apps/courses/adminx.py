# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 17:46'


import xadmin
from .models import Course,Lesson,Video,CourseResource

# 这里要继承object，不能继承models.Model


class CourseAdmin(object):
    # 显示的字段列
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num','add_time']
    # 搜索
    search_fields = ['name','desc','detail','degree','students','fav_nums','image','click_num']
    # 过滤器
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image','click_num','add_time']


class LessonAdmin(object):
    list_display = ['name','course','add_time']
    search_fields = ['name','course']
    # 外键如何处理，如果只写course，则不能显示，如果想显示，则需要写成course__name(字段名)
    list_filter = ['name','course__name','add_time']

class VideoAdmin(object):
    list_display = ['name','lesson','add_time']
    search_fields = ['name','lesson']
    list_filter = ['name','lesson__name','add_time']


class CourseResourceAdmin(object):
    list_display = ['name','course','download','add_time']
    search_fields = ['name','course','download']
    list_filter = ['name','course__name','download','add_time']

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)