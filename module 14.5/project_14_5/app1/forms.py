from django import forms
from datetime import date
from django.forms.widgets import NumberInput

CHOICES = [
    ("web_design", "Web Design"),
    ("seo", "Search Engine Optimization"),
    ("content_creation", "Content Creation"),
    ("social_media", "Social Media Management"),
    ("branding", "Branding"),
]


class MyForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=10,
        widget=forms.TextInput(attrs={"class": "bg-black text-white"}),
    )
    email = forms.EmailField(label="Email", required=False, initial="name@gmail.com")
    log = forms.BooleanField(label="Keep Login", initial=True)
    day = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    services = forms.MultipleChoiceField(widget=c,choices=CHOICES)
    top_service = forms.ChoiceField(label="Top Service", choices=CHOICES)
