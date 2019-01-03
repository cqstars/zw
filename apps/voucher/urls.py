# -*- coding: utf-8 -*-
# @Time    : 2018-12-28 20:14
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views
app_name = 'voucher'
urlpatterns = [
    path('voucher', views.IndexView.as_view(), name='voucher'),
    path('', views.index, name='index'),
]