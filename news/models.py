from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()

