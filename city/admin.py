from django.contrib import admin
from django.contrib.admin import site

from city.models import City, CityCar


class CityAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CityCarAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'citytitle', 'car_id', 'modelcar', 'available_cars')
    list_filter = ('city_id', 'car_id', 'available_cars')
    search_fields = ('city_id', 'car_id')
    ordering = ('city_id', 'car_id')


site.register(City, CityAdmin)
site.register(CityCar, CityCarAdmin)