from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text="Номер телефона")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']



class CallbackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    phone = forms.CharField(max_length=15, required=True, help_text='Введите номер телефона')


