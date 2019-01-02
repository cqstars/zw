from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(AccountingSubjectCategory)
class AccountingSubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

@admin.register(AccountingSubject)
class AccountingSubjectAdmin(admin.ModelAdmin):
    list_display = ('AccountingSubjectNo','name','scopeofapplication','dr_amount','cr_amount','category')
    list_per_page = 50
    ordering = ('id',)

@admin.register(AccountingSubject_2)
class AccountingSubject_2Admin(admin.ModelAdmin):
    list_display = ('subject2_no', 'name', 'scopeofapplication', 'dr_amount', 'cr_amount', 'subject')
    list_per_page = 50
    ordering = ('id',)