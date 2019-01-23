# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View


from AccountingSubjects.models import AccountingSubject, AccountingSubject_2, AccountingSubjectCategory
from .models import *
from ledger.models import *
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
        msg = ""
        if f.is_valid():
            # 验证过后f.cleaned_data[key]干净的数据
            voucherkey = ['date', 'voucher_no', 'accounting_supervisor', 'enclosure', 'total_dr', 'total_cr',
                          'book_keepinger', 'cashier', 'auditor', 'order_makinger', 'isbookkeeping']
            voucherobj = dict([(key, f.cleaned_data[key]) for key in voucherkey])
            try:
                print(voucherobj)
                v = voucher.objects.create(**voucherobj)
                # v.objects.id

            except Exception as e:
                AS = AccountingSubjectCategory.objects.all()
                return render(request, 'voucher/voucher_input.html', {"AS": AS, "msg": e})
            else:
                # 逐条插入
                for i in range(8):
                    i = i + 1
                    vc_content_key = ['vc_bf_' + str(i), 'vc_ac_' + str(i), 'vc_ac2_' + str(i), 'vc_dr_' + str(i),
                                      'vc_cr_' + str(i), 'vc_isBookkeeping_' + str(i)]
                    vc_content_obj = dict([(key, f.cleaned_data[key]) for key in vc_content_key])
                    # 提交的数据全部为真vc_content_obj是明细内容
                    if vc_content_obj["vc_bf_" + str(i)] and vc_content_obj["vc_ac_" + str(i)] and (
                            vc_content_obj["vc_dr_" + str(i)] or vc_content_obj["vc_cr_" + str(i)]):
                        vc_content_obj["brife"] = vc_content_obj.pop("vc_bf_" + str(i))
                        vc_content_obj["accountingsubject"] = AccountingSubject.objects.get(
                            id=vc_content_obj["vc_ac_" + str(i)])
                        if (vc_content_obj["vc_ac2_" + str(i)]):
                            vc_content_obj["accountingsubject_2"] = AccountingSubject_2.objects.get(
                                id=vc_content_obj["vc_ac2_" + str(i)])
                        else:
                            vc_content_obj["accountingsubject_2"] = None
                        vc_content_obj["dr_amount"] = vc_content_obj.pop("vc_dr_" + str(i))
                        vc_content_obj["cr_amount"] = vc_content_obj.pop("vc_cr_" + str(i))
                        vc_content_obj["isbookkeeping"] = vc_content_obj.pop("vc_isBookkeeping_" + str(i))
                        vc_content_obj["voucher_no"] = voucher.objects.get(id=v.id)
                        del vc_content_obj['vc_ac_' + str(i)]
                        del vc_content_obj['vc_ac2_' + str(i)]
                        voucher_content.objects.create(**vc_content_obj)
                    else:
                        msg += "栏目" + str(i) + "录入无有效内容！"
                AS = AccountingSubjectCategory.objects.all()
                msg += "凭证录入成功！"
                return render(request, 'voucher/voucher_input.html', {"AS": AS, "msg": msg})
        else:
            AS = AccountingSubjectCategory.objects.all()
            return render(request, "voucher/voucher_input.html", {"AS": AS, "f": f})


class voucherlistView(ListView):
    model = voucher
    template_name = 'voucher/voucher_list.html'
    context_object_name = 'voucher_list'

def bookkeep(request,id):
    iskeep=voucher_content.objects.get(id=id)
    if iskeep.isbookkeeping:
        return HttpResponse(False)
    else:
        if iskeep.accountingsubject_2:
            sl=subsidiary_ledger()
            sl.date=iskeep.voucher_no.date
            sl.description=iskeep.brife
            sl.voucher_no=iskeep.voucher_no
            sl.gen_led_ac=iskeep.accountingsubject
            sl.sub_led_ac=iskeep.accountingsubject_2
            if iskeep.dr_amount:
                sl.dr_amount=iskeep.dr_amount
            else:
                sl.dr_amount=0
                sl.dr_or_cr='cr'
            if iskeep.cr_amount:
                sl.cr_amount=iskeep.cr_amount
            else:
                sl.cr_amount=0
                sl.dr_or_cr='dr'
            try:
                sl.save()
                iskeep.isbookkeeping = True
                iskeep.save()
            except:
                return HttpResponse(False)
            else:
                return HttpResponse(True)



        else:
            ledger_=ledger()
            ledger_.date=iskeep.voucher_no.date
            ledger_.description=iskeep.brife
            ledger_.voucher_no=iskeep.voucher_no
            ledger_.accountno=iskeep.accountingsubject
            if iskeep.dr_amount:
                ledger_.dr_amount=iskeep.dr_amount
            else:
                ledger_.dr_amount=0
                ledger_.dr_or_cr='cr'
            if iskeep.cr_amount:
                ledger_.cr_amount=iskeep.cr_amount
            else:
                ledger_.cr_amount=0
                ledger_.dr_or_cr='dr'
            try:
                ledger_.save()
                iskeep.isbookkeeping = True
                iskeep.save()
            except:
                return HttpResponse(False)
            else:
                return HttpResponse(True)










