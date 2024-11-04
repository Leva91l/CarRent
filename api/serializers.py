from rest_framework import serializers

from cars.models import Car
from rent.models import Rent


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'model', 'year', 'price')


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ('start_date', 'end_date', 'car', 'city')


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ('returned',)
