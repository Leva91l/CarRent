from django import forms

from rent.models import Rent


class RentForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Rent
        fields = ('start_date', 'end_date', 'car', 'city')



class ReturnCarForm(forms.ModelForm):
    returned = forms.BooleanField(label='')

    class Meta:
        model = Rent
        fields = ('returned',)