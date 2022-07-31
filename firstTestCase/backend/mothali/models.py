from django.db import models

# Create your models here.
class Newsfeed(models.Model):
    userid=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    media = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Questions(models.Model):
    userid=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    answers=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)