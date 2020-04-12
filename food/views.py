from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions

from food.models import Order, Ingredients, IngredientsClass
from food.serializers import (
    OrderSerializer, IngredientsSerializer, IngredientsClassSerializer
)


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class IngredientsListCreateView(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAuthenticated]


class IngredientsClassListCreateView(generics.ListCreateAPIView):
    queryset = IngredientsClass.objects.all()
    serializer_class = IngredientsClassSerializer
    permission_classes = [IsAuthenticated]

