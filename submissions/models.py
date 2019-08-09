from django.db import models

# Create your models here.

LANG = [
    ('C', 'C'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Python3', 'Python3'),
]

STATUS = [
    (-1, 'No status'),
    (0, 'Solution accepted'),
    (1, 'Solution rejected'),
    (2, 'Compilation error'),
    (3, 'Runtime error'),
    (4, 'Execution error'),
    (5, 'Time-limit exceeded'),
    (6, 'Memory-limit exceeded')
]


class Submission(models.Model):
    userid = models.IntegerField(blank=False)
    when = models.DateTimeField(auto_now_add=True)
    lang = models.CharField(max_length=10, choices=LANG, blank=False)
    problemid = models.IntegerField(blank=False)
    timetaken = models.IntegerField(default=500)
    memorytaken = models.IntegerField(default=128)
    code = models.TextField(max_length=40000, blank=False)
    status = models.CharField(max_length=30, default=-1)
