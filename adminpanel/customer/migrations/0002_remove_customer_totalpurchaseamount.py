# Generated by Django 4.1.1 on 2022-11-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='totalpurchaseamount',
        ),
    ]
