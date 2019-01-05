# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.views.generic import View

from AccountingSubjects.models import AccountingSubject,AccountingSubject_2,AccountingSubjectCategory
# Create your views here.
def index(request):
    AS=AccountingSubjectCategory.objects.all()
    return render(request,"voucher/voucher.html",{"AS":AS})


class voucher_make(View):
    def get(self,request,*args,**kwargs):
        AS = AccountingSubjectCategory.objects.all()
        return render(request, "voucher/voucher.html", {"AS": AS})
    def post(self,requset):
        pass

class IndexView(generic.ListView):
    template_name = "voucher/voucher.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        e=AccountingSubject.objects.get(id=1)
        c=e.category
        return c