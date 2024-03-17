from django import forms
from datetime import date


class MyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(label="Email", required=False, initial="name@gmail.come"),
    
    log = forms.BooleanField(label="Keep Login"))
    # day = forms.DateField(initial=date.today),
