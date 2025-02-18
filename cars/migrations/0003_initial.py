# Generated by Django 5.1.2 on 2024-10-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_delete_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет')),
                ('engine', models.FloatField(blank=True, null=True, verbose_name='Двигатель')),
                ('engine_power', models.IntegerField(blank=True, null=True, verbose_name='Объем двигателя')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Авто',
                'verbose_name_plural': 'Авто',
                'ordering': ['price', 'year', '-price'],
            },
        ),
    ]
