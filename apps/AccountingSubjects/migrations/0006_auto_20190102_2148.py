# Generated by Django 2.1.4 on 2019-01-02 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountingSubjects', '0005_auto_20190102_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingsubject',
            name='scopeofapplication',
            field=models.CharField(max_length=30, verbose_name='会计科目适用范围'),
        ),
        migrations.AlterField(
            model_name='accountingsubject_2',
            name='scopeofapplication',
            field=models.CharField(max_length=30, verbose_name='会计科目适用范围'),
        ),
    ]
