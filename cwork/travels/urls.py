from django.urls import path, include
from . import views


urlpatterns = [
    path('main/', views.main),
    path('offers/<slug:slug_city_offers>', views.city_offers, name='city_offers-detail'),
]