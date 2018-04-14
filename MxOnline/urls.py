"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyView
import xadmin
import captcha

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    # url(r"^login$",TemplateView.as_view(template_name='login.html'),name='login'),
    url(r'^login$',LoginView.as_view(),name='login'),
    url(r'^register$',RegisterView.as_view(),name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)$',ActiveUserView.as_view(),name='active'),
    url(r'^forget$',ForgetPwdView.as_view(),name='forgetpwd'),
    url(r'^reset/(?P<reset_code>.*)$',ResetView.as_view(),name='reset'),
    url(r'^modifypwd$',ModifyView.as_view(),name='modifypwd'),
]
