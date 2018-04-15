# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-15 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180414_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='catgory',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y/%m', verbose_name='logo'),
        ),
    ]
