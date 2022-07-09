from django.contrib import admin
from .models import City, Offer


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'name', 'slug']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug' : ('title', )}