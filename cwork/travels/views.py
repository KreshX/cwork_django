from django.shortcuts import render, get_object_or_404
from .models import City, Offer

def main(request):
	cities = City.objects.all()

	return render(request, 'travels/main.html' , {'cities': cities})


def city_offers(request, slug_city_offers:str):
	city_offers = get_object_or_404(City, slug=slug_city_offers)
	offers = Offer.objects.all()
	return render(request, 'travels/city_offers.html', {'city_offers': city_offers, 'offers': offers})