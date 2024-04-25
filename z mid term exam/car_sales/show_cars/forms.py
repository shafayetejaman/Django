from .models import Car, Brand,Comment
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        