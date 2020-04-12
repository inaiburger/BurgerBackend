from django.urls import include, path

from food.views import OrderListCreateView, IngredientsClassListCreateView, IngredientsListCreateView

api_urlpatterns = [
    path("order/", OrderListCreateView.as_view(), name="order"),
    path("ingredientsclass/", IngredientsClassListCreateView.as_view(), name="ingredientsclass"),
    path('ingredients/', IngredientsListCreateView.as_view(), name='ingredients'),
]

