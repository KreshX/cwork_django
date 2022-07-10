from django.db import models
from django.urls import reverse



class Offer(models.Model):

	title = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	# 

	# def get_url(self):
	# 	return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'



class City(models.Model):

	name = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	# offers = models.ForeignKey(Offer, on_delete=models.PROTECT, null=True, blank=True)
	def get_url(self):
		return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.name}'


class Service(models.Model):

	title = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	offers = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
	price = models.IntegerField(default='10325')
	def get_url(self):
		return reverse('tour-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'


class Order(models.Model):
	service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=40)
	number = models.CharField(max_length=40)
	def __str__(self):
		return f'{self.service}'

	def get_url(self):
		return reverse('order-update', args=[self.slug])