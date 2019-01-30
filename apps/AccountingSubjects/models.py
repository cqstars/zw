from django.db import models

# Create your models here.
class AccountingSubjectCategory(models.Model):
    name=models.CharField(max_length=10,verbose_name="会计科目分类名称")

    class Meta:
        verbose_name = "会计科目大类"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
    def get_accountingsubject(self):
        return self.accountingsubject_set.all()
    def get_myacset(self):
        return self.myaccountingsubject_set.all()

class AccountingSubject(models.Model):
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
        return self.accountingsubject_2_set.all()


class AccountingSubject_2(models.Model):
    subject=models.ForeignKey(AccountingSubject,on_delete=models.CASCADE,verbose_name="会计科目")
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