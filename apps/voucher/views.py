# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from AccountingSubjects.models import AccountingSubject,AccountingSubject_2,AccountingSubjectCategory
# Create your views here.
def index(request):
    AS=AccountingSubjectCategory.objects.all()
    return render(request,"voucher/voucher.html",{"AS":AS})

class IndexView(generic.ListView):
    template_name = "voucher/voucher.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        e=AccountingSubject.objects.get(id=1)
        c=e.category
        return c