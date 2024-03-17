from django import forms
from datetime import datetime


class MyForm(forms.Form):
    name = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(required=False, initial="name@gmail.come"),
    day = forms.DateField(initial=datetime.date.today)
