from django.shortcuts import render, get_object_or_404
from .models import City, Offer, Service

def main(request):
	cities = City.objects.all()

	return render(request, 'travels/main.html' , {'cities': cities})


def city_offers(request, slug_city_offers:str):
	city_offers = get_object_or_404(City, slug=slug_city_offers)
	services = Service.objects.filter(offers=city_offers.id)
	return render(request, 'travels/city_offers.html', {'city_offers': city_offers, 'services': services})

def tour(request, slug_tour:str):
	service = get_object_or_404(Service, slug=slug_tour)
	return render(request, 'travels/tour.html', {'service': service})

def login(request):
	return render(request, 'travels/login.html')	