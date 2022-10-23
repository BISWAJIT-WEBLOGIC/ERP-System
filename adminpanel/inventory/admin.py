from django.contrib import admin

from .models import Product_Category, Product


@admin.register(Product_Category)
class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_ID', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'Product_Name',
        'Product_ID',
        'category',
        'Product_Stock',
        'image',
    )
    list_filter = ('category',)