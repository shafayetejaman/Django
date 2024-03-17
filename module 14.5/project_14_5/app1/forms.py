from django import forms
from datetime import date
from django.forms.widgets import NumberInput


class MyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(label="Email", required=False, initial="name@gmail.com")
    log = forms.BooleanField(label="Keep Login", initial=True)
    day = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
