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
    path('voucher_make', views.voucher_make.as_view(), name='voucher_make'),
    path('voucher_make_form', views.voucher_formView.as_view(), name='voucher_make_form'),
    path('', views.index, name='index'),
]