# -*- coding: utf-8 -*-
# @Time    : 2019-01-21 10:08
# @Author  : 彭涛
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'ledger'
urlpatterns = [
    path('ledgerlist', views.ledgerListView.as_view(), name='ledgerlist'),
    path('ledgersetupaccountingsubject1/<int:id>/', views.ledgersetupaccountingsubject1, name='ledgersetupaccountingsubject1'),
    path('ledgersetup', views.ledgersetupView.as_view(), name='ledgersetup'),
    # path('account_subject_by_categoryid/<int:id>/', views.account_subject_by_categoryid,name='account_subject_by_categoryid'),
]
