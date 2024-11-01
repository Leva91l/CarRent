from rent.views import CarRentView, RentPanelView, rent_delete
from django.urls import path

urlpatterns = [
    path('carrent/<slug:slug>', CarRentView.as_view(), name='carrent'),
    path('rent_panel', RentPanelView.as_view(), name='rent_panel'),
    path('rent_delete/<int:pk>', rent_delete, name='rent_delete'),

]