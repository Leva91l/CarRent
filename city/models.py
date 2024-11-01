from django.db import models


class City(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название города')
    slug = models.SlugField(unique=True, verbose_name='URL', max_length=20, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        ordering = ['title']


class CityCar(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='ID города')
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, verbose_name='ID авто')
    available_cars = models.IntegerField(default=0, verbose_name='Свободные машины')

    class Meta:
        verbose_name = 'Машины по городам'
        verbose_name_plural = 'Машины по городам'
        ordering = ['available_cars']

    def modelcar(self):
        return self.car.model

    def citytitle(self):
        return self.city.title