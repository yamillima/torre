from django.db import models
from django.utils import timezone


class Search(models.Model):
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
