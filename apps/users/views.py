from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


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
    def post(self,request):
        # if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        # django自带的认证
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request, 'login.html',{'errmsg':'用户名或密码错误'})
        # elif request.method == 'GET':
    def get(self,request):
        return render(request,'login.html')
