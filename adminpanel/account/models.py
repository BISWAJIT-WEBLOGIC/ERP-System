from email.policy import default
from .manager import UserManager
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser ,PermissionsMixin
)


class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    ph_number = models.IntegerField( blank=True, null=True,default=None)
    address = models.TextField( blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # this field is required to login super user from admin panel
    staff = models.BooleanField(default=False)
    # this field is required to login super user from admin panel
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin