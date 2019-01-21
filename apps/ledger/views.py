from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# Create your views here.


class IndexView(ListView):
    model = subsidiary_ledger
    template_name = 'blog/index.html'
    context_object_name = 'post_list'