from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=15)
    github_link = models.CharField(max_length=30)
    view_count = models.IntegerField()

class Stack(models.Model):
    resume = models.ForeignKey(Resume)
    development_language = models.CharField(max_length=30)
