from django.db import models

# Create your models here.


class Problem(models.Model):
    author = models.CharField(
        max_length=50, blank=False, unique=False)
    title = models.CharField(
        max_length=100, blank=False, unique=False)
    statement = models.TextField(
        max_length=10000, blank=False, unique=False)
    timelimit = models.IntegerField(
        blank=False, unique=False, default=1000)
    memorylimit = models.IntegerField(
        blank=False, unique=False, default=256)
    score = models.IntegerField(blank=False, unique=False)
    tag = models.CharField(
        max_length=100, blank=False, unique=False)
    attempts = models.IntegerField(
        blank=False, unique=False, default=0)
    successes = models.IntegerField(
        blank=False, unique=False, default=0)

    def __str__(self):
        return self.title
