from django.contrib import admin
from .models import City, Service, Order
from django.db.models import QuerySet
from django.contrib.auth.models import User


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display = [ 'id', 'name', 'slug']
	list_editable = [ 'name','slug']
	prepopulated_fields = {'slug' : ('name', )}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'slug', 'offers', 'price', 'currency']
	list_editable = ['title', 'slug', 'offers', 'price']
	prepopulated_fields = {'slug' : ('title', )}
	actions = ['set_rubles']

	@admin.action(description = 'Установить валюту в рубли')
	def set_rubles(self, request, qs:QuerySet):
		count_updated = qs.update(currency=Service.RUB)
		self.message_user(request,f'Было обновлено {count_updated} записей')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'service','name', 'number']
	list_editable = ['service','name', 'number']



admin.site.site_header = 'Админка тур-компании'
admin.site.index_title = 'Тур-компания: Вокруг света'