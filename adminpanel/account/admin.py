from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# from members.forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User
from django.utils.translation import gettext_lazy  as _
from .form import GroupAdminForm


class UserAdmin(BaseUserAdmin):

    
    list_display = ( 'email','first_name','last_name',
                    'staff','ph_number','address','designation')
    list_filter = ('id',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name',
                                     'staff',)}),
        (_('Permissions'), {'fields': ('is_superuser',
                                       'groups', 'user_permissions',)}),
    )
    # filter_horizontal = ('groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name',  'staff')}
         ),
    )
    search_fields = ('email', 'first_name')
    ordering = ('first_name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)