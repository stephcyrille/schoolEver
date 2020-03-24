import datetime

from django.db import models
from django.utils import timezone


class Ue(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default='000')
    description = models.CharField(max_length=200, default='')
    level = models.CharField(max_length=10, default='')
    semester = models.CharField(max_length=10, default='')
    teacher = models.CharField(max_length=10, blank=True)
    lecture_hour = models.IntegerField(default=1)
    tp_hour = models.IntegerField(default=1)
    status = models.CharField(max_length=10, default='CLOSE')
    create_by = models.CharField(max_length=100, default='')
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - (%s) " % (self.title, self.code)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now