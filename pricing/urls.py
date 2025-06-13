from django.urls import path
from .views import calculate_prices

urlpatterns = [
    path('calculate/', calculate_prices, name='calculate'),
]
