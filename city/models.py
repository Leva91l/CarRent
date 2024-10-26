from django.db import models

from cars.models import Car


class City(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class CityCar(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    available_cars = models.IntegerField(default=0)
