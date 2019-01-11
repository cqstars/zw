# -*- coding: utf-8 -*-
# @Time    : 2019-01-09 17:41
# @Author  : 彭涛
# @Site    : 
# @File    : form.py
# @Software: PyCharm
from django import forms
from django.forms import widgets
from django.forms import fields

class vocher_form(forms.Form):
    voucher_no=forms.CharField(label="字第",max_length=5,widget=widgets.TextInput(attrs={'class':"form-control"}))
    date=forms.DateField(label="日期")
