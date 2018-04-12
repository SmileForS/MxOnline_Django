from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .forms import LoginForm

# Create your views here.
from django.views.generic import View
from .models import UserProfile

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None

class Login(View):
    def get(self,request):
        """显示页面"""
        return render(request,'login.html')

    def post(self,request):
        """登录验证"""
        login_form = LoginForm(request.POST)    # 需要一个参数，字典类型，request.POST里就是一个字典，这其实也是对表单的一种验证（因为有对字段的约束）
        if login_form.is_valid():

            username = request.POST.get('username','')
            password = request.POST.get('password','')
            # django自带的认证
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'index.html')
            else:
                return render(request,'login.html',{'errmsg':'用户或密码错误'})
        else:
            return render(request, 'login.html',{'login_form':login_form})

