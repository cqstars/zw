# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
from .form import *

from AccountingSubjects.models import AccountingSubject, AccountingSubject_2, AccountingSubjectCategory
from .form import *


# Create your views here.
def index(request):
    AS = AccountingSubjectCategory.objects.all()
    return render(request, "voucher/voucher.html", {"AS": AS})


class voucher_make(View):
    def get(self, request, *args, **kwargs):
        AS = AccountingSubjectCategory.objects.all()
        return render(request, "voucher/voucher.html", {"AS": AS})

    def post(self, requset):
        voucher_no = requset.POST.get("voucher_no", "")
        voucherdate = requset.POST.get("voucherdate", "")
        pass


class IndexView(generic.ListView):
    template_name = "voucher/voucher.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        e = AccountingSubject.objects.get(id=1)
        c = e.category
        return c


class voucher_input(View):

    def get(self, request):
        # vocherform=vocher_form()
        # vochercontentForm=vochercontentFormSet()
        AS = AccountingSubjectCategory.objects.all()
        return render(request, 'voucher/voucher_input.html', {"AS": AS})

    def post(self, request):
        f = vocher_input_fom(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            voucherkey = ['date', 'voucher_no','accounting_supervisor','enclosure', 'total_dr','total_cr','book_keepinger','cashier','auditor','order_makinger','isbookkeeping']
            voucherobj = dict([(key, f.cleaned_data[key]) for key in voucherkey ])
            try:
                print(voucherobj)
                v=voucher.objects.create(**voucherobj)
                # v.objects.id

            except Exception as e:
                AS = AccountingSubjectCategory.objects.all()
                return render(request, 'voucher/voucher_input.html', {"AS": AS,"msg":e})
            else:
                vc_content_list = []
                vc_content_1 = ['vc_bf_1', 'vc_ac_1', 'vc_ac2_1', 'vc_dr_1', 'vc_cr_1', 'vc_isBookkeeping_1']
                vc_content_1_obj = dict([(key, f.cleaned_data[key]) for key in vc_content_1])
                vc_content_1_obj["brife"] = vc_content_1_obj.pop("vc_bf_1")
                vc_content_1_obj["accountingsubject"] = AccountingSubject.objects.get(id=vc_content_1_obj["vc_ac_1"])
                if(vc_content_1_obj["vc_ac2_1"]):
                    vc_content_1_obj["accountingsubject_2"] = AccountingSubject_2.objects.get(id=vc_content_1_obj["vc_ac2_1"])
                else:
                    vc_content_1_obj["accountingsubject_2"]=None
                vc_content_1_obj["dr_amount"] = vc_content_1_obj.pop("vc_dr_1")
                vc_content_1_obj["cr_amount"] = vc_content_1_obj.pop("vc_cr_1")
                vc_content_1_obj["isbookkeeping"] = vc_content_1_obj.pop("vc_isBookkeeping_1")
                vc_content_1_obj["voucher_no"] = voucher.objects.get(id=v.id)
                del vc_content_1_obj['vc_ac_1']
                del vc_content_1_obj['vc_ac2_1']
                vc_content_list.append(vc_content_1_obj)
                voucher_content.objects.create(**vc_content_1_obj)
                # voucher_content.objects.bulk_create(vc_content_list)
                AS = AccountingSubjectCategory.objects.all()
                return render(request, 'voucher/voucher_input.html', {"AS": AS,"msg":"凭证录入成功！"})
        else:
            AS = AccountingSubjectCategory.objects.all()
            return render(request, "voucher/voucher_input.html", {"AS": AS, "f": f})
