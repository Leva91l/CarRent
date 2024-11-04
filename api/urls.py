from rest_framework import routers

from django.urls import path

from api import views
from api.views import AdminAPIUpdate

router = routers.DefaultRouter()

router.register(r'cars', views.CarViewSet, basename='cars')
router.register(r'rent', views.RentViewSet, basename='rents')


urlpatterns = [
    path('adminupdate/<int:pk>/', AdminAPIUpdate.as_view()),

]