# Generated by Django 4.1.1 on 2022-10-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('totalpurchaseamount', models.IntegerField(blank=True, default=0, null=True)),
                ('ph_number', models.IntegerField(blank=True, default=None, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
