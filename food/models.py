from django.db import models
from people.models import UserInfo


class Order(models.Model):
    owner = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class IngredientsClass(models):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    price_100g = models.IntegerField()
    order = models.ManyToManyField(Order)
    ingredientsclass = models.ForeignKey(IngredientsClass,
                                         on_delete=models.CASCADE,
                                         related_name='%(class)s')

    def __str__(self):
        return self.name
