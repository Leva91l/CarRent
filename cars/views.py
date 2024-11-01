from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from CarRent.utils import CallbackMixin
from cars.forms import RegistrationForm, CallbackForm
from cars.mail import send_mail
from cars.models import Car, Profile


def index(request):
    cars = Car.objects.all()
    forma = CallbackForm()
    context = {'cars': cars, 'forma': forma}
    return render(request, 'home.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, phone=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, pasword=raw_password)
            return redirect('home')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


class ProfileView(CallbackMixin, ListView):
    template_name = 'profile.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix = self.get_user_context()
        context = dict(list(context.items()) + list(mix.items()))
        return context


class CarView(CallbackMixin, ListView):
    model = Car
    template_name = 'cars/cars.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        mix = self.get_user_context()
        context = dict(list(context.items()) + list(mix.items()))
        return context

def callback(request):
    if request.method == 'POST':
            send_mail(request.POST['name'], 'levapython@yandex.ru', request.POST['phone'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
