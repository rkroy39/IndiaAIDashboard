
# core/models.py
from django.db import models
from django.utils.timezone import now
import threading

_user = threading.local()

def get_current_user():
    return getattr(_user, 'value', None)

class CommonFields(models.Model):
    created_on = models.DateTimeField(default=now, editable=False)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'self', null=True, blank=True,
        related_name="%(class)s_created", on_delete=models.SET_NULL
    )
    modified_by = models.ForeignKey(
        'self', null=True, blank=True,
        related_name="%(class)s_modified", on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk and not self.created_by:
            self.created_by = user
        self.modified_by = user
        super().save(*args, **kwargs)
        
class RoleMaster(CommonFields):
    role_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Role Master"
        verbose_name_plural = "Role Masters"

    def __str__(self):
        return self.role_name
