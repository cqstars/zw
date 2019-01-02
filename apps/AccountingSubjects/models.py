from django.db import models

# Create your models here.
class AccountingSubjectCategory(models.Model):
    name=models.CharField(max_length=10,verbose_name="会计科目分类名称")

    class Meta:
        verbose_name = "会计科目大类"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class AccountingSubject(models.Model):
    category=models.ForeignKey(AccountingSubjectCategory,on_delete=models.CASCADE,verbose_name="会计科目大类")
    AccountingSubjectNo=models.CharField(max_length=5,verbose_name="编号")
    name=models.CharField(max_length=15,verbose_name="会计科目名称")
    scopeofapplication=models.CharField(max_length=15,verbose_name="会计科目适用范围")

    class Meta:
        verbose_name = "会计科目"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name