# Generated by Django 4.1.1 on 2022-10-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default=120, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='inventory', verbose_name='Product Image'),
        ),
    ]
