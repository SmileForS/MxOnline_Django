# -*- coding:utf-8 -*-
__author__ = 'LL'
__date__ = '2018/4/12 23:19'

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """创建form表单"""
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=8)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=8)
    captcha = CaptchaField()
