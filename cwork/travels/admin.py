from django.contrib import admin
from .models import City, Offer, Service


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'name', 'slug']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug' : ('title', )}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug' : ('title', )}