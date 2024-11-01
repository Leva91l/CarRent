from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name='Цвет')
    engine = models.FloatField(blank=True, null=True,verbose_name='Объем двигателя')
    engine_power = models.IntegerField(blank=True, null=True, verbose_name='Мощность двигателя')
    year = models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')
    image = models.ImageField(upload_to='images/cars', verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=20, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'
        ordering = ['price', 'year', '-price']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
