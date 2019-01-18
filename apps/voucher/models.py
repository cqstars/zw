from django.db import models
from AccountingSubjects.models import AccountingSubject,AccountingSubject_2
# Create your models here.
class voucher(models.Model):
    voucher_no=models.CharField(max_length=10,verbose_name="字 第 号")
    date=models.DateField(verbose_name="凭证日期")
    enclosure=models.IntegerField(default=0,verbose_name="附件")
    total_dr=models.DecimalField(default=0,max_digits=11,decimal_places=2,verbose_name="借方金额")
    total_cr=models.DecimalField(default=0,max_digits=11,decimal_places=2,verbose_name="贷方金额")
    accounting_supervisor=models.CharField(max_length=12,verbose_name="会计主管")
    book_keepinger=models.CharField(blank=True,null=True,max_length=12,verbose_name="记账")
    cashier=models.CharField(blank=True,null=True,max_length=12,verbose_name="出纳")
    auditor=models.CharField(blank=True,null=True,max_length=12,verbose_name="审核")
    order_makinger=models.CharField(max_length=12,verbose_name="制单")
    isbookkeeping = models.BooleanField(blank=True,null=True,verbose_name="记账√")

    class Meta:
        verbose_name = "凭证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.voucher_no

class voucher_content(models.Model):
    voucher_no=models.ForeignKey(voucher,on_delete=models.CASCADE,verbose_name="凭证号码",blank=True,null=True,)
    brife=models.CharField(max_length=50,verbose_name="摘要",blank=True,null=True,)
    accountingsubject=models.ForeignKey(AccountingSubject,on_delete=models.CASCADE,verbose_name="会计科目",blank=True,null=True)
    accountingsubject_2=models.ForeignKey(AccountingSubject_2,on_delete=models.CASCADE,verbose_name="会计科目二级",blank=True,null=True)
    dr_amount = models.DecimalField(blank=True,null=True,max_digits=11, decimal_places=2, default=0, verbose_name="借方金额")
    cr_amount = models.DecimalField(blank=True,null=True,max_digits=11, decimal_places=2, default=0, verbose_name="贷方金额")
    isbookkeeping=models.BooleanField(blank=True,null=True)
    class Meta:
        verbose_name = "凭证具体内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.brife