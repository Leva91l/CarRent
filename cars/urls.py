from django.urls import path

from cars.views import index, registration, ProfileView, CarView

urlpatterns = [
    path('', index, name='home'),
    path('registration/', registration, name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cars/', CarView.as_view(), name='cars'),

    # path('callback/', callback, name='callback'),
]
