from django.db import models
from django.utils import timezone


class Search(models.Model):
    text = models.CharField(max_length=500)
    jobsid = models.TextField(default=0)
    date = models.DateTimeField(default=timezone.now)
