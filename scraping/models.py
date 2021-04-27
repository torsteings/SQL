from django.db import models
# Create your models here.
class Job(models.Model):
    url = models.CharField(max_length=80)
