from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login),
    path('login/', views.login,name='login'),
    path('register/', views.login, name='register'),
    path('main/', views.main),
    path('offers/<slug:slug_city_offers>', views.city_offers, name='city_offers-detail'),
    path('offer/<slug:slug_tour>', views.tour, name='tour-detail'),

]