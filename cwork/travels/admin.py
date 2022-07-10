from django.contrib import admin
from .models import City, Service, Order


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'name', 'slug']
	list_editable = [ 'name','slug']
	prepopulated_fields = {'slug' : ('name', )}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'offers', 'price']
	list_editable = ['title', 'slug', 'offers', 'price']
	prepopulated_fields = {'slug' : ('title', )}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'service','name', 'number']
	list_editable = ['service','name', 'number']