# -*- coding: utf-8 -*-
# @Time    : 2019-01-03 12:36
# @Author  : 彭涛
# @Site    : 
# @File    : url.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'AccountingSubject'
urlpatterns = [
    path('', views.index, name='index'),
    path('account_subject_by_categoryid/<int:id>/', views.account_subject_by_categoryid,name='account_subject_by_categoryid'),
]
