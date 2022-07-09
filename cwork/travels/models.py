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
	offers = models.ForeignKey(Offer, on_delete=models.PROTECT, null=True, blank=True)
	def get_url(self):
		return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.name}'


class Service(models.Model):

	title = models.CharField(max_length=40)
	slug = models.SlugField(default='', null=False, blank=True)
	offers = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
	# def get_url(self):
	# 	return reverse('city_offers-detail', args=[self.slug])

	def __str__(self):
		return f'{self.title}'