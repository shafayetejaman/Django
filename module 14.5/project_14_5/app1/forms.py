from django import forms
from datetime import date


class MyForm(forms.Form):
    name = forms.CharField(
        label="Name"
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(label="" required=False, initial="name@gmail.come"),
    day = forms.DateField(initial=date.today)
    log = forms.BooleanField(label="Keep Login")
