from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .forms import LoginForm,RegisterForm
from django.views.generic import View
from .models import UserProfile,EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email

class CustomBackend(ModelBackend):
    """"用户认证"""
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None

class ActiveUserView(View):
    """激活链接"""
    def get(self,request,active_code):
        # 查询记录是否存在
        try:
            records = EmailVerifyRecord.objects.filter(code=active_code)
        except Exception as e:
            print(e)
            return render(request,'register.html',{'errmsg':'激活失败，请重新激活'})
        if records:
            for record in records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()

        else:
            return render(request, 'active_fail.html')
        return render(request,'login.html')







class RegisterView(View):
    """注册验证"""
    def get(self,request):
        """显示"""
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email', '')
            # 判断email是否已经被注册
            if UserProfile.objects.filter(email=username):
                return render(request,'register.html',{'register_form':register_form,'errmsg':'用户已经存在'})

            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = username
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()

            send_register_email(username,'register')
            return redirect(reverse('login'))
        else:
            return render(request,'register.html',{'register_form':register_form})




class LoginView(View):
    """登录"""
    def get(self,request):
        """显示页面"""
        return render(request,'login.html')

    def post(self,request):
        """登录验证"""
        # 初始化form表单
        login_form = LoginForm(request.POST)    # 需要一个参数，字典类型，request.POST里就是一个字典，这其实也是对表单的一种验证（因为有对字段的约束）
        if login_form.is_valid():

            username = request.POST.get('username','')
            password = request.POST.get('password','')
            # django自带的认证
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request,'index.html')
                else:
                    return render(request, 'login.html', {'errmsg': '用户未激活'})
            else:
                return render(request,'login.html',{'errmsg':'用户或密码错误'})
        else:
            return render(request, 'login.html',{'login_form':login_form})

# class Logout(View):
