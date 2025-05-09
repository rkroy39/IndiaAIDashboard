from django.db import models
from django.contrib.auth.models import User
from core.models import CommonFields

class LoginAuditTrail(CommonFields):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    username_attempted = models.CharField(max_length=150)
    success = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.username_attempted} at {self.created_on} - {'Success' if self.success else 'Failed'}"