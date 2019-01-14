# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
from .form import *

from AccountingSubjects.models import AccountingSubject,AccountingSubject_2,AccountingSubjectCategory
from .form import *
# Create your views here.
def index(request):
    AS=AccountingSubjectCategory.objects.all()
    return render(request,"voucher/voucher.html",{"AS":AS})


class voucher_make(View):
    def get(self,request,*args,**kwargs):
        AS = AccountingSubjectCategory.objects.all()
        return render(request, "voucher/voucher.html", {"AS": AS})
    def post(self,requset):
        voucher_no = requset.POST.get("voucher_no", "")
        voucherdate= requset.POST.get("voucherdate", "")
        pass

class IndexView(generic.ListView):
    template_name = "voucher/voucher.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        e=AccountingSubject.objects.get(id=1)
        c=e.category
        return c

class voucher_formView(View):
    def get(self,request):
        form=vocher_form()
        return render(request, 'voucher/test.html', {'form': form})
    def post(self,request):
        f = vocher_form(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            return render(request,'voucher/voucher_make_form.html', {'form': f})
        else:
            return render(request, "voucher/voucher_make_form.html", {"error": f.errors, "form": f})