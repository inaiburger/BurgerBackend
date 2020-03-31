from django.db import models
from people.models import UserInfo


class Post(models.Model):
    title = models.CharField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
