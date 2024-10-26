from django.contrib import admin

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'engine', 'engine_power', 'price', 'image')
    list_filter = ('brand', 'model', 'year', 'color', 'engine', 'engine_power', 'price')
    search_fields = ('brand', 'model')
    prepopulated_fields = {'slug': ('model',)}


admin.site.register(Car, CarAdmin)