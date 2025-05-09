# core/models.py
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
import threading
from simple_history.models import HistoricalRecords

_user = threading.local()

def get_current_user():
    return getattr(_user, 'value', None)

class CommonFields(models.Model):
    created_on = models.DateTimeField(default=now, editable=False)
    modified_on = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)


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

