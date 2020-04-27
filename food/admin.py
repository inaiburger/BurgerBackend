from django.contrib import admin
from food.models import Order, Ingredients, IngredientsClass


class OrderAdmin(admin.ModelAdmin):
    model = Order


admin.site.register(Order)
admin.site.register(IngredientsClass)
admin.site.register(Ingredients)
