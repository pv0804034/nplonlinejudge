from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(upload_to='images/', blank=False)
    rating = models.PositiveIntegerField(blank=False)
    score = models.PositiveIntegerField(default=0)
    played = models.PositiveIntegerField(blank=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default="About myself")
    address = models.CharField(max_length=100, default="Nepal")
