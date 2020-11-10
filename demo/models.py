from django.db import models

# Create your models here.
class Course(models.Model):
    professor = models.CharField(max_length=36, default='')
    className = models.CharField(max_length=36, default='')
    section = models.IntegerField()
