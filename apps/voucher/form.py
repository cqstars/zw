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
    enclosure=forms.IntegerField(required=False,error_messages={"invalid": "格式错误"})
    accounting_supervisor=forms.CharField(max_length=12,required=True,error_messages={"required": "主管签字不能为空","invalid": "格式错误","max_length": "主管太长"})
    voucher_no=forms.CharField(max_length=10,required=True,error_messages={"required": "不能为空","invalid": "格式错误","max_length": "凭证编码太长"})
    book_keepinger=forms.CharField(required=False,max_length=12,error_messages={"invalid": "格式错误","max_length": "人名不大于六字符"})
    cashier=forms.CharField(required=False,max_length=12,error_messages={"invalid": "格式错误","max_length": "人名不大于六字符"})
    auditor=forms.CharField(required=False,max_length=12,error_messages={"invalid": "格式错误","max_length": "人名不大于六字符"})
    order_makinger=forms.CharField(label="制单人",max_length=12,error_messages={"invalid": "格式错误","max_length": "人名不大于六字符"})
    total_dr = forms.DecimalField(required=False, max_digits=11, decimal_places=2)
    total_cr = forms.DecimalField(required=False, max_digits=11, decimal_places=2)
    isbookkeeping = forms.BooleanField(required=False)

    vc_bf_1=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_1=forms.IntegerField(required=False)
    vc_ac2_1=forms.IntegerField(required=False)
    vc_dr_1=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_1=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_1=forms.BooleanField(required=False)

    vc_bf_2=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_2 = forms.IntegerField(required=False)
    vc_ac2_2 = forms.IntegerField(required=False)
    vc_dr_2=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_2=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_2= forms.BooleanField(required=False)

    vc_bf_3=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_3 = forms.IntegerField(required=False)
    vc_ac2_3 = forms.IntegerField(required=False)
    vc_dr_3=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_3=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_3 = forms.BooleanField(required=False)

    vc_bf_4=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_4 = forms.IntegerField(required=False)
    vc_ac2_4 = forms.IntegerField(required=False)
    vc_dr_4=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_4=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_4= forms.BooleanField(required=False)

    vc_bf_5=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_5= forms.IntegerField(required=False)
    vc_ac2_5 = forms.IntegerField(required=False)
    vc_dr_5=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_5=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_5 = forms.BooleanField(required=False)

    vc_bf_6=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_6 = forms.IntegerField(required=False)
    vc_ac2_6 = forms.IntegerField(required=False)
    vc_dr_6=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_6=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_6 = forms.BooleanField(required=False)

    vc_bf_7=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_7 = forms.IntegerField(required=False)
    vc_ac2_7 = forms.IntegerField(required=False)
    vc_dr_7=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_7=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_7 = forms.BooleanField(required=False)

    vc_bf_8=forms.CharField(required=False,max_length=50,error_messages={"invalid": "格式错误","max_length": "摘要超过了50个字符"})
    vc_ac_8 = forms.IntegerField(required=False)
    vc_ac2_8 = forms.IntegerField(required=False)
    vc_dr_8=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_cr_8=forms.DecimalField(required=False,max_digits=11,decimal_places=2)
    vc_isBookkeeping_8 = forms.BooleanField(required=False)

4