from django.db import models

from AccountingSubjects.models import AccountingSubjectCategory,AccountingSubject,AccountingSubject_2
from voucher.models import voucher,voucher_content

# Create your models here.
class myaccountingsubject(models.Model):
    category=models.ForeignKey(AccountingSubjectCategory,on_delete=models.CASCADE,verbose_name="会计科目大类")
    AccountingSubjectNo=models.CharField(max_length=8,verbose_name="编号")
    name=models.CharField(max_length=15,verbose_name="会计科目名称")
    dr_amount=models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name="借方金额")
    cr_amount=models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name="贷方金额")
    scopeofapplication=models.CharField(max_length=30,verbose_name="会计科目适用范围")

    class Meta:
        verbose_name = "会计科目"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
    def get_accountingsubject_2(self):
        return self.myaccountingsubject_2_set.all()


class myaccountingsubject_2(models.Model):
    subject=models.ForeignKey(myaccountingsubject,on_delete=models.CASCADE,verbose_name="会计科目")
    subject2_no=models.CharField(max_length=12,verbose_name="编号")
    name=models.CharField(max_length=15,verbose_name="会计科目二级名称")
    dr_amount=models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name="借方金额")
    cr_amount=models.DecimalField(max_digits=9,decimal_places=2,default=0,verbose_name="贷方金额")
    scopeofapplication=models.CharField(max_length=30,verbose_name="会计科目适用范围")

    class Meta:
        verbose_name = "会计科目二级"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class ledger(models.Model):
    date = models.DateField(verbose_name="凭证日期")
    description = models.CharField(max_length=50, verbose_name="摘要", blank=True, null=True)
    accountno=models.ForeignKey(AccountingSubject,on_delete=models.CASCADE,verbose_name="总帐科目",blank=True,null=True)
    voucher_no = models.ForeignKey(voucher, on_delete=models.CASCADE, verbose_name="凭证字号", blank=True, null=True)
    description = models.CharField(max_length=50, verbose_name="摘要", blank=True, null=True )
    dr_amount = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2, default=0,verbose_name="借方金额")
    cr_amount = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2, default=0,verbose_name="贷方金额")
    dr_or_cr=models.CharField(max_length=2,verbose_name="借或贷",choices=(("dr","借"),("cr","贷")))


    class Meta:
        verbose_name = "总分类账"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.accountno


class subsidiary_ledger(models.Model):
    date = models.DateField(verbose_name="凭证日期")
    gen_led_ac=models.ForeignKey(AccountingSubject,on_delete=models.CASCADE,verbose_name="总帐科目",blank=True,null=True)
    sub_led_ac=models.ForeignKey(AccountingSubject_2,on_delete=models.CASCADE,verbose_name="明细科目",blank=True,null=True)
    voucher_no = models.ForeignKey(voucher, on_delete=models.CASCADE, verbose_name="凭证字号", blank=True, null=True)
    description = models.CharField(max_length=50, verbose_name="摘要", blank=True, null=True )
    dr_amount = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2, default=0,verbose_name="借方金额")
    cr_amount = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=2, default=0,verbose_name="贷方金额")
    dr_or_cr=models.CharField(max_length=2,verbose_name="借或贷",choices=(("dr","借"),("cr","贷")))

    class Meta:
        verbose_name = "明细分类账"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gen_led_ac.name



