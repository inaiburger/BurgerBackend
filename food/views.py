from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from food.permissions import CustomDjangoModelPermissions

from food.models import Order, Ingredients, IngredientsClass
from food.serializers import (
    OrderSerializer, IngredientsSerializer, IngredientsClassSerializer
)


class OrderListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        CustomDjangoModelPermissions,
    )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class IngredientsListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        CustomDjangoModelPermissions,
    )
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class IngredientsClassListCreateView(generics.ListCreateAPIView):
    permission_classes = (
        CustomDjangoModelPermissions,
    )
    queryset = IngredientsClass.objects.all()
    serializer_class = IngredientsClassSerializer
