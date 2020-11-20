from django.db import models

# Create your models here.
class Course(models.Model):
    professor = models.CharField(max_length=256, blank=True)
    className = models.CharField(max_length=256, blank=False)
    section = models.IntegerField()

    def __str__(self):
        return self.className

class Note(models.Model):
    title = models.CharField(max_length=32, blank=False)
    date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title