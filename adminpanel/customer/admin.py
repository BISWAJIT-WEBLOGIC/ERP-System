from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','customer_Id',  'email', 'ph_number', 'address')
    search_fields = ('name',)