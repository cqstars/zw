# Generated by Django 2.1.4 on 2019-01-02 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AccountingSubjects', '0002_auto_20181229_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountingsubject',
            name='cr_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='贷方金额'),
        ),
        migrations.AddField(
            model_name='accountingsubject',
            name='dr_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='借方金额'),
        ),
        migrations.AlterField(
            model_name='accountingsubject',
            name='AccountingSubjectNo',
            field=models.CharField(max_length=5, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='accountingsubject',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AccountingSubjects.AccountingSubjectCategory', verbose_name='会计科目大类'),
        ),
        migrations.AlterField(
            model_name='accountingsubject',
            name='name',
            field=models.CharField(max_length=15, verbose_name='会计科目名称'),
        ),
        migrations.AlterField(
            model_name='accountingsubject',
            name='scopeofapplication',
            field=models.CharField(max_length=15, verbose_name='会计科目适用范围'),
        ),
        migrations.AlterField(
            model_name='accountingsubjectcategory',
            name='name',
            field=models.CharField(max_length=10, verbose_name='会计科目分类名称'),
        ),
    ]
