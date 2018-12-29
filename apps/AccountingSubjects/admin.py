from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(AccountingSubjectCategory)
class AccountingSubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

@admin.register(AccountingSubject)
class AccountingSubjectAdmin(admin.ModelAdmin):
    list_display = ('AccountingSubjectNo','name','scopeofapplication','category')
    list_per_page = 50
    ordering = ('id',)