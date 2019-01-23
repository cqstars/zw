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
    path('voucherlist', views.voucherlistView.as_view(), name='voucherlist'),
    path('bookkeep/<int:id>/', views.bookkeep, name='bookkeep'),
    path('voucher_input', views.voucher_input.as_view(), name='voucher_input'),
    path('', views.index, name='index'),
]
