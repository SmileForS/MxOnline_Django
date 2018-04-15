from django.shortcuts import render
from django.views.generic import View


class OrgListView(View):
    """课程机构视图"""
    def get(self,request):
        """显示页面"""
        return render(request,'org-list.html')