from django.shortcuts import render, get_object_or_404
from .models import City, Offer, Service, Order
from django.http import HttpResponseRedirect
from .forms import OrderForm
from django.views.generic import UpdateView
from django.db.models import F, Sum, Min, Max,Count, Avg

def main(request):
	cities = City.objects.all()

	return render(request, 'travels/main.html' , {'cities': cities})


def city_offers(request, slug_city_offers:str):
	city_offers = get_object_or_404(City, slug=slug_city_offers)
	services = Service.objects.filter(offers=city_offers.id)
	agg = services.aggregate(Avg('price'), Max('price'), Min('price'))
	return render(request, 'travels/city_offers.html', {'city_offers': city_offers, 'agg':agg, 'services': services})

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


def list_order(request):
	orders = Order.objects.all()
	return render(request, 'travels/list_order.html' , {'orders': orders, 'total': orders.count()})


class NewsUpdateView(UpdateView):
	model = Order
	template_name = 'travels/update.html'
	fields = ['number']