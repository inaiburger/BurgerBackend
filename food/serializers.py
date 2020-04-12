from rest_framework import serializers
from food.models import Order, IngredientsClass, Ingredients


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = '__all__'


class IngredientsClassSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True)

    class Meta:
        model = IngredientsClass
        fields = '__all__'
