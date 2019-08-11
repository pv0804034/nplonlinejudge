from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(
        upload_to='images/', default='images/profile-image-placeholder.png', blank=True)
    rating = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    played = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, default="About myself")
    address = models.CharField(max_length=100, default="Nepal")
    organization = models.CharField(max_length=100, blank=True)
