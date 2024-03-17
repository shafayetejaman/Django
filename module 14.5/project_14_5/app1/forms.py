from django import forms


class MyForm(forms.Form):
    name = forms.CharField(
        max_length=10, widget=forms.CharField(attrs={"class": "bg-black text-white"})
    )
