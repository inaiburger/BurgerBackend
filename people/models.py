from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    news_latter_sub = models.BooleanField(default=False)

    def __str__(self):
        return '%d: %s %s' % (self.user.id, self.user.first_name, self.user.last_name)
