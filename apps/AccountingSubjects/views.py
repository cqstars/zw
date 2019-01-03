from django.shortcuts import render,render_to_response
from .models import *

# Create your views here.
def index(request4):
    AS=AccountingSubjectCategory.objects.all()
    return render_to_response("AccountingSubject/index.html",{"AS":AS})

def test(request,id):
    id=id
    return render_to_response("AccountingSubject/2.html",{"id":id})