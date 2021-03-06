from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField(max_length=15, default="Please enter the name")
    body = models.TextField()
    

    def __str__(self):
        return self.title