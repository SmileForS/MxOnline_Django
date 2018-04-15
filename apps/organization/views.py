from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import CourseOrg,CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

class OrgListView(View):
    """课程机构视图"""
    def get(self,request):
        """显示页面"""
        # 获取参数,取出筛选城市
        city_id = request.GET.get('city','')
        ct = request.GET.get('ct','')
        sort = request.GET.get('sort','')

        try:
            course_orgs = CourseOrg.objects.all()
            hot_orgs = course_orgs.order_by('-click_nums')[:3]
            cities = CityDict.objects.all()

            if city_id:
                # 在结果集中进行进一步筛选
                course_orgs = course_orgs.filter(city_id=int(city_id))
            # 类别筛选
            if ct:
                course_orgs = course_orgs.filter(catgory=ct)

            if sort:
                if sort == 'students':
                    course_orgs = course_orgs.order_by('-students')
                elif sort == 'courses':
                    course_orgs = course_orgs.order_by('-course_nums')
            org_nums = course_orgs.count()
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
            'city_id':city_id,
            'ct':ct,
            'hot_orgs':hot_orgs,
            'sort':sort,
        }
        return render(request,'org-list.html',context)
