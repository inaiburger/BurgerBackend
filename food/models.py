from django.db import models
from people.models import UserInfo


class Order(models.Model):
    owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class Ingredients(models.Model):
    name = models.CharField()
    price_100g = models.IntegerField()
    order = models.ManyToManyField(Order)
