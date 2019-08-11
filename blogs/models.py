from django.db import models
from django.conf import settings

# Create your models here.


class Blog(models.Model):
    author = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100000, blank=False)
