
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
import threading
from simple_history.models import HistoricalRecords

_user = threading.local()

class NavigationBar(models.Model):
    
    page_name = models.CharField(max_length=255, unique=True)
    page_url = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(default=now, editable=False)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_by', null=True, blank=True)
    modified_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='modified_by', null=True, blank=True)
    