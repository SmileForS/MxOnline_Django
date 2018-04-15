from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CourseOrg,CityDict

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

        else:
            context = {
                'course_orgs':course_orgs,
                'cities':cities,
                'org_nums':org_nums,
            }
            return render(request,'org-list.html',context)
