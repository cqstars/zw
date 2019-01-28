from django.shortcuts import render, HttpResponse
from django.views.generic import View, ListView

from .models import *
from AccountingSubjects.models import *


# Create your views here.

class ledgersetupView(View):
    def get(self, request):
        AS = AccountingSubjectCategory.objects.all()
        return render(request, 'ledger/ledgersetup.html', {"AS": AS})

    def post(self, request):
        aid = request.POST.get("aid")
        bid = request.POST.get("bid")

        if bid:
            accountsubject_inquery = AccountingSubject.objects.get(id=aid)
            accountsubject2_inquery = AccountingSubject_2.objects.get(id=bid)
            result = myaccountingsubject.objects.filter(AccountingSubjectNo=accountsubject_inquery.AccountingSubjectNo)
            if result:
                result2 = myaccountingsubject_2.objects.filter(subject2_no=accountsubject2_inquery.subject2_no)
                if result2.exists():
                    return HttpResponse(accountsubject2_inquery.name + "这个二级科目已经设置过了")
                else:
                    newmyac2 = myaccountingsubject_2()
                    newmyac2.subject = myaccountingsubject.objects.get(
                        AccountingSubjectNo=accountsubject_inquery.AccountingSubjectNo)
                    newmyac2.subject2_no= accountsubject2_inquery.subject2_no
                    newmyac2.dr_amount = accountsubject2_inquery.dr_amount
                    newmyac2.cr_amount = accountsubject2_inquery.cr_amount
                    newmyac2.name = accountsubject2_inquery.name
                    newmyac2.scopeofapplication = accountsubject2_inquery.scopeofapplication
                    newmyac2.save()
                return HttpResponse("科目设置成功")

            else:
                newmyac = myaccountingsubject()
                newmyac.category = accountsubject_inquery.category
                newmyac.AccountingSubjectNo = accountsubject_inquery.AccountingSubjectNo
                newmyac.dr_amount = accountsubject_inquery.dr_amount
                newmyac.cr_amount = accountsubject_inquery.cr_amount
                newmyac.name = accountsubject_inquery.name
                newmyac.scopeofapplication = accountsubject_inquery.scopeofapplication
                newmyac.save()
                result2 = myaccountingsubject_2.objects.filter(subject2_no=accountsubject2_inquery.subject2_no)
                if result2.exists():
                    return HttpResponse(accountsubject2_inquery.name + "这个二级科目已经设置过了")
                else:
                    newmyac2 = myaccountingsubject_2()
                    newmyac2.subject = newmyac
                    newmyac2.subjectNo = accountsubject2_inquery.subject2_no
                    newmyac2.dr_amount = accountsubject2_inquery.dr_amount
                    newmyac2.cr_amount = accountsubject2_inquery.cr_amount
                    newmyac2.name = accountsubject2_inquery.name
                    newmyac2.scopeofapplication = accountsubject2_inquery.scopeofapplication
                    newmyac2.save()
                return HttpResponse("科目设置成功")
        else:
            accountsubject_inquery = AccountingSubject.objects.get(id=aid)
            result = myaccountingsubject.objects.filter(AccountingSubjectNo=accountsubject_inquery.AccountingSubjectNo)
            if result.exists():
                return HttpResponse(accountsubject_inquery.name + "这个一级科目已经设置过了")

            else:
                newmyac = myaccountingsubject()
                newmyac.category = accountsubject_inquery.category
                newmyac.AccountingSubjectNo = accountsubject_inquery.AccountingSubjectNo
                newmyac.dr_amount = accountsubject_inquery.dr_amount
                newmyac.cr_amount = accountsubject_inquery.cr_amount
                newmyac.name = accountsubject_inquery.name
                newmyac.scopeofapplication = accountsubject_inquery.scopeofapplication
                newmyac.save()
                return HttpResponse("科目设置成功")

def ledgersetupaccountingsubject1(requset, id):
    a = AccountingSubject.objects.filter(id=id)
    # ledger.objects.filter(a).create(a)
    return HttpResponse("ok")


class ledgerListView(View):
    def get(self, request):
        # ledger_list_= ledger.objects.values("accountno").distinct()

        ledger_list = AccountingSubject.objects.filter(id__in=['2', '226', '54'])
        return render(request, "ledger/ledgerlist.html", {"ledger_list": ledger_list})
