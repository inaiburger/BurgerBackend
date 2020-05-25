from django.db import models
from django.contrib.auth.models import User


class IngredientsClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    price_100g = models.IntegerField()
    image = models.FileField(upload_to='ingredients/', help_text='Image of ingredients')
    ingredientsclass = models.ForeignKey(IngredientsClass,
                                         on_delete=models.CASCADE,
                                         related_name='%(class)s')

    def __str__(self):
        return self.name


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)
    status = models.BooleanField(default=False)

