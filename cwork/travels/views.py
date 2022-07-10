from django.shortcuts import render, get_object_or_404
from .models import City, Offer, Service, Order
from django.http import HttpResponseRedirect
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def main(request):
	cities = City.objects.all()

	return render(request, 'travels/main.html' , {'cities': cities})


def city_offers(request, slug_city_offers:str):
	city_offers = get_object_or_404(City, slug=slug_city_offers)
	services = Service.objects.filter(offers=city_offers.id)
	return render(request, 'travels/city_offers.html', {'city_offers': city_offers, 'services': services})

def tour(request, slug_tour:str):
	service = get_object_or_404(Service, slug=slug_tour)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			# a = get_object_or_404(Service, slug=slug_tour)
			feed = Order( service = get_object_or_404(Service, slug=slug_tour),
				name=form.cleaned_data['name'],
				number=form.cleaned_data['number'],
				)
			feed.save()
			return HttpResponseRedirect('/admin')
	else:
		form = OrderForm()
	return render(request, 'travels/tour.html', context={'form': form, 'service': service})
	# return render(request, 'travels/tour.html', {'service': service})

def login(request):
	# if request.method == 'POST':
	# 	form = OrderForm(request.POST)
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		feed = Order(service=Service.objects.all()[0],
	# 			name=form.cleaned_data['name'],
	# 			number=form.cleaned_data['number'],
	# 			)
	# 		feed.save()
	# 		return HttpResponseRedirect('admin')
	# else:
	# 	form = OrderForm()
	return render(request, 'travels/login.html')
	# return render(request, 'travels/login.html')	



class RegisterUser(CreateView):
	form_class = UserCreationForm
	template_name = 'travels/register.html'
	success_url = reverse_lazy('login')