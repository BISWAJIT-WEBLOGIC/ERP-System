# Generated by Django 4.1.1 on 2022-11-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('OFD', 'out for delivery'), ('IP', 'In-progress'), ('C', 'Complete'), ('R', 'Return')], default='IP', max_length=10),
        ),
    ]