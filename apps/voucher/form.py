# -*- coding: utf-8 -*-
# @Time    : 2019-01-09 17:41
# @Author  : 彭涛
# @Site    : 
# @File    : form.py
# @Software: PyCharm
from django import forms
from django.forms import widgets
from django.forms import fields
from  django.forms import ModelForm
from django.forms import inlineformset_factory

from .models import *

class vocher_form(ModelForm):
    class Meta:
        model = voucher
        fields = ("voucher_no","date","enclosure","total_dr","total_cr","accounting_supervisor","book_keepinger","cashier","auditor","order_makinger","isbookkeeping",)


vochercontentFormSet=inlineformset_factory(voucher,voucher_content,fields=("brife","accountingsubject","accountingsubject_2",),extra=3, can_delete=False, max_num=5)
class vocher_input_fom(forms.Form):
    date=forms.DateField(required=True,error_messages={"required": "不能为空","invalid": "格式错误","min_length": "用户名最短8位"})
    accounting_supervisor=forms.CharField(max_length=20,required=True,error_messages={"required": "主管签字不能为空","invalid": "格式错误","max_length": "主管太长"})
    voucher_no=forms.CharField(max_length=10,required=True,error_messages={"required": "不能为空","invalid": "格式错误","max_length": "凭证编码太长"})
    vc_bf_1=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_1=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_1=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_2=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_2=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_2=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_3=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_3=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_3=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_4=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_4=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_4=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_5=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_5=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_5=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_6=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_6=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_6=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_7=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_7=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_7=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_bf_8=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_dr_8=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_8=forms.DecimalField(required=False,max_digits=11,decimal_places=2)

4