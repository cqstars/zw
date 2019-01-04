from django.shortcuts import render,render_to_response
from .models import *

# Create your views here.

def index(request4):
    ASC=AccountingSubjectCategory.objects.all()
    return render_to_response("AccountingSubject/index.html",{"ASC":ASC})

def test(request,id):
    AccountingSubjectCategoryid=id
    as_c=AccountingSubjectCategory.objects.get(id=AccountingSubjectCategoryid)
    a=as_c.accountingsubject_set.all()
    return render_to_response("AccountingSubject/2.html",{"AS":a})