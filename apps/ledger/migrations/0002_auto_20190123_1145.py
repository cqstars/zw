# Generated by Django 2.1.4 on 2019-01-23 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='ledger',
            name='isbookkeeping',
        ),
        migrations.RemoveField(
            model_name='subsidiary_ledger',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='subsidiary_ledger',
            name='isbookkeeping',
        ),
    ]