from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CourseOrg,CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class OrgListView(View):
    """课程机构视图"""
    def get(self,request):
        """显示页面"""
        try:
            course_orgs = CourseOrg.objects.all()
            org_nums = course_orgs.count()
            cities = CityDict.objects.all()
        except CourseOrg.DoesNotExist:
            return redirect(reverse('index'))
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation
        # 参数1：要分页的对象（可迭代），参数2：每页几个，参数3（固定）：request = request
        p = Paginator(course_orgs,3, request=request)

        course_orgs = p.page(page)

        context = {
            'course_orgs':course_orgs,
            'cities':cities,
            'org_nums':org_nums,
        }
        return render(request,'org-list.html',context)
