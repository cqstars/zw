# Generated by Django 2.1.4 on 2019-02-01 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0005_auto_20190130_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='accountno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountingSubjects.myaccountingsubject', verbose_name='总帐科目'),
        ),
        migrations.AlterField(
            model_name='subsidiary_ledger',
            name='gen_led_ac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountingSubjects.myaccountingsubject', verbose_name='总帐科目'),
        ),
        migrations.AlterField(
            model_name='subsidiary_ledger',
            name='sub_led_ac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AccountingSubjects.myaccountingsubject_2', verbose_name='明细科目'),
        ),
    ]
