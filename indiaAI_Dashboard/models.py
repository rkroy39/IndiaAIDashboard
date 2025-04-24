# accounts/models.py
from django.db import models
from core.models import CommonFields, RoleMaster
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser, CommonFields):
    roles = models.ManyToManyField(RoleMaster, related_name="users", blank=True)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
