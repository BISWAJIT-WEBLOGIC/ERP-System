from django.contrib import admin

from .models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = (
        'machine_ID',
        'machine_name',
        'machine_current_temperature',
    )